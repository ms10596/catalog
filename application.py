#!/usr/bin/python

from flask import Flask, render_template, request, redirect, jsonify
from flask import session as login_session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
import random
import string
import httplib2
import json
import requests

app = Flask(__name__)
CLIENT_ID = json.loads(
    open('/var/www/catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "catalog"
engine = create_engine('sqlite:////var/www/catalog/catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def homepage():
    """
    Returns Homepage for a visitor or a signed-in user.
    Depends on the login session id
    """
    categories = session.query(Category)
    movies = session.query(Item, Category).join(Category)\
        .order_by(Item.id.desc()).limit(10).all()
    if 'id' in login_session:
        user = session.query(User)\
            .filter(User.id == login_session['id']).first()
        return render_template('loggedInMenu.html',
                               categories=categories,
                               movies=movies, email=user.email)
    else:
        return render_template('menu.html',
                               categories=categories, movies=movies)


@app.route('/catalog/<string:categoryName>/items/')
def categoryPage(categoryName):
    """
    Returns page of items related to the given category name
    :param categoryName:
    """
    items = session.query(Item, Category)\
        .join(Category).filter(Category.name == categoryName).all()
    return render_template('categoryItems.html', items=items)


@app.route('/catalog/<string:categoryName>/<string:itemName>/')
def itemPage(categoryName, itemName):
    """
    Returns page of a specific item from a specific category
    :param categoryName:
    :param itemName:
    """
    description = session.query(Item, Category)\
        .join(Category).filter(Category.name == categoryName)\
        .filter(Item.name == itemName).one()
    if 'id' in login_session and \
            description.Item.userId == login_session['id']:
        return render_template('authItem.html', description=description)
    else:
        return render_template('item.html', description=description)


@app.route('/catalog/add/', methods=['GET', 'POST'])
def addPage():
    """
    Return the Add Item page that allows signedin user to add items
    """
    if request.method == 'POST':
        if 'id' in login_session:
            newItem = Item()
            if request.form['category']:
                newItem.categoryId = session.query(Category)\
                    .filter(Category.name == request.form['category']).one().id
            if request.form['name']:
                newItem.name = request.form['name']
            if request.form['description']:
                newItem.description = request.form['description']
            newItem.userId = login_session['id']

            session.add(newItem)
            session.commit()

        flash("new item has been added")

        return redirect('/', code=302)
    else:
        return render_template('addItem.html')


@app.route('/catalog/<string:itemName>/edit/', methods=['GET', 'POST'])
def editPage(itemName):
    """
    Returns page that allows authorised user to edit an item
    :param itemName:
    """
    if request.method == 'POST':
        item = session.query(Item).filter_by(name=itemName).one()
        if 'id' in login_session and login_session['id'] == item.userId:
            if request.form['category']:
                item.categoryId = session.query(Category)\
                    .filter(Category.name == request.form['category']).one()
            if request.form['name']:
                item.name = request.form['name']
            if request.form['description']:
                item.description = request.form['description']
            session.add(item)
            session.commit()
        return redirect('/', code=302)
    else:
        item = session.query(Item).filter_by(name=itemName).one()
        if 'id' in login_session and login_session['id'] != item.userId:
            return redirect('/', code=302)
        return render_template('editItem.html')


@app.route('/catalog/<string:itemName>/delete/', methods=['GET', 'POST'])
def deletePage(itemName):
    """
     Returns page that allows authorised user to delete an item
    :param itemName:
    """
    if request.method == 'POST':
        item = session.query(Item).filter_by(name=itemName).one()
        if 'id' in login_session and login_session['id'] == item.userId:
            session.delete(item)
            session.commit()
        return redirect('/', code=302)
    else:
        item = session.query(Item).filter_by(name=itemName).one()
        if 'id' in login_session and login_session['id'] == item.userId:
            return render_template('deleteItem.html')
        return redirect('/', code=302)


@app.route('/catalog.json/')
def jsonFile():
    """
    Returns json object of the whole data
    """
    items = session.query(Item, Category).join(Category).order_by(Category.id)
    return jsonify(items=[i.Item.serialize for i in items])


@app.route('/catalog.json/<string:categoryName>/items/')
def categoryJson(categoryName):
    """
    Returns json of items related to the given category name
    :param categoryName:
    """
    items = session.query(Item, Category)\
        .join(Category).filter(Category.name == categoryName).all()
    return jsonify(items=[i.Item.serialize for i in items])


@app.route('/catalog.json/<string:itemName>/')
def itemPagejson(itemName):
    """
    Returns json of a specific item from a specific category
    :param categoryName:
    :param itemName:
    """
    description = session.query(Item, Category)\
        .join(Category).filter(Item.name == itemName).one()
    return jsonify(description.Item.serialize)


@app.route('/catalog/register/', methods=['GET', 'POST'])
def register():
    """
    Return page that allows new visitors to sign up in the website
    Should have a google account
    """
    if request.method == 'POST':
        newUser = User(email=request.form['email'],
                       name=request.form['name'],
                       password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('registerUser.html')


@app.route('/catalog/login/')
def showLogin():
    """
    Returns login page and create a state
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('loginUser.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """
    Authenticate the logged in user through google login and OAuth2
    """
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print
        "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    currentUser = session.query(User)\
        .filter(User.email == data['email']).first()
    if (currentUser is None):
        currentUser = User(email=data['email'],
                           name=data['name'],
                           password='password')
        session.add(currentUser)
        session.commit()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['id'] = currentUser.id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: ' \
              '150px;-webkit-border-radius: 150px;-moz-border-radius: ' \
              '150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print
    "done!"
    return output


@app.route('/catalog/logout/')
def gdisconnect():
    """
    Logout the logged in user
    """
    access_token = login_session.get('access_token')
    if access_token is None:
        print
        'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print
    'In gdisconnect access token is %s', access_token
    print
    'User name is: '
    print
    login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' \
          '' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print
    'result is '
    print
    result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['id']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect('/', code=302)
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'hello'
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python

from flask import Flask, render_template, request, redirect, url_for, jsonify, session as login_session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def homepage():
    categories = session.query(Category)
    movies = session.query(Item, Category).join(Category).all()
    if ('id' in login_session):
        return render_template('loggedInMenu.html', categories=categories, movies=movies)
    else:
        return render_template('menu.html', categories=categories, movies=movies)


@app.route('/catalog/<string:categoryName>/items/')
def categoryPage(categoryName):
    items = session.query(Item, Category).join(Category).filter(Category.name == categoryName).all()
    return render_template('categoryItems.html', items=items)


@app.route('/catalog/<string:categoryName>/<string:itemName>/')
def itemPage(categoryName, itemName):
    description = session.query(Item, Category).join(Category).filter(Category.name == categoryName).filter(Item.name == itemName).one()
    print (login_session['id'] )
    print (description.Item.userId)
    if 'id' in login_session and description.Item.userId == login_session['id']:
        return render_template('authItem.html', description=description)
    else:
        return render_template('item.html', description=description)



@app.route('/catalog/add/', methods=['GET', 'POST'])
def addPage():
    if (request.method == 'POST'):
        id = login_session['id']
        categoryid = session.query(Category).filter(Category.name == request.form['category']).one()
        loginUser = session.query(User).one()
        print(loginUser)
        newItem = Item(name=request.form['name'], categoryId=categoryid.id,
                       description=request.form['description'], userId=loginUser.id)
        session.add(newItem)
        session.commit()
        flash("nw item has been added")
        return redirect('/catalog/add/', code=302)
    else:
        return render_template('addItem.html')


@app.route('/catalog/<string:itemName>/edit/', methods=['GET', 'POST'])
def editPage(itemName):
    if (request.method == 'POST'):
        item = session.query(Item).filter_by(name=itemName).one()
        if(login_session['id'] != item.userId):
            return redirect('/', code=302)
        item.name = request.form['name']
        item.category = request.form['category']
        item.description = request.form['description']
        session.add(item)
        session.commit()
        return redirect('/', code=302)
    else:
        item = session.query(Item).filter_by(name=itemName).one()
        if (login_session['id'] != item.userId):
            return redirect('/', code=302)
        return render_template('editItem.html')


@app.route('/catalog/<string:itemName>/delete/', methods=['GET', 'POST'])
def deletePage(itemName):
    if (request.method == 'POST'):
        item = session.query(Item).filter_by(name=itemName).one()
        if (login_session['id'] != item.userId):
            return redirect('/', code=302)
        session.delete(item)
        session.commit()
        return redirect('/', code=302)
    else:
        item = session.query(Item).filter_by(name=itemName).one()
        if (login_session['id'] != item.userId):
            return redirect('/', code=302)
        return render_template('deleteItem.html')


@app.route('/catalog.json/')
def json():
    items = session.query(Item, Category).join(Category)
    return jsonify(items=[i.serialize for i in items])


@app.route('/catalog/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        newUser = User(email=request.form['email'], name=request.form['name'], password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('registerUser.html')


@app.route('/catalog/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginUser = session.query(User).filter(User.email == request.form['email']).filter(User.password == request.form['password']).one()
        if loginUser:
            login_session['id'] = loginUser.id
            flash("logged in")
            return redirect('/', code=302)
        else:
            flash("try again")
            return render_template('loginUser.html')
    else:
        flash("welcome")
        return render_template('loginUser.html')


@app.route('/catalog/logout/')
def logout():
    login_session.pop('id')
    flash("logged out")
    return redirect('/', code=302)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'hello'
    app.run(host='0.0.0.0', port=8000)

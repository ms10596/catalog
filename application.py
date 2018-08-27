#!/usr/bin/python

from flask import Flask, render_template, request, redirect, jsonify, session as login_session, flash
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
    movies = session.query(Item, Category).join(Category).order_by(Item.id.desc()).limit(10).all()
    if 'id' in login_session:
        user = session.query(User).filter(User.id == login_session['id']).one()
        return render_template('loggedInMenu.html', categories=categories, movies=movies, email=user.email)
    else:
        return render_template('menu.html', categories=categories, movies=movies)


@app.route('/catalog/<string:categoryName>/items/')
def categoryPage(categoryName):
    items = session.query(Item, Category).join(Category).filter(Category.name == categoryName).all()
    return render_template('categoryItems.html', items=items)


@app.route('/catalog/<string:categoryName>/<string:itemName>/')
def itemPage(categoryName, itemName):
    description = session.query(Item, Category).join(Category).filter(Category.name == categoryName).filter(
        Item.name == itemName).one()
    if 'id' in login_session and description.Item.userId == login_session['id']:
        return render_template('authItem.html', description=description)
    else:
        return render_template('item.html', description=description)


@app.route('/catalog/add/', methods=['GET', 'POST'])
def addPage():
    if request.method == 'POST':
        if 'id' in login_session:
            newItem = Item()
            if request.form['category']:
                newItem.categoryId = session.query(Category).filter(Category.name == request.form['category']).one().id
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
    if request.method == 'POST':
        item = session.query(Item).filter_by(name=itemName).one()
        if 'id' in login_session and login_session['id'] == item.userId:
            if request.form['category']:
                item.categoryId = session.query(Category).filter(Category.name == request.form['category']).one()
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
def json():
    items = session.query(Item, Category).join(Category).order_by(Category.id)
    return jsonify(items=[i.Item.serialize for i in items])


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
        loginUser = session.query(User).filter(User.email == request.form['email']).filter(
            User.password == request.form['password']).one()
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

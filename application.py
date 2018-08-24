from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def homepage():
    categories = session.query(Item.category).distinct()
    movies = session.query(Item).order_by(Item.id.desc()).all()
    return render_template('menu.html', categories=categories, movies=movies)


@app.route('/catalog/<string:categoryName>/items')
def categoryPage(categoryName):
    items = session.query(Item.name).filter_by(category=categoryName)
    return render_template('categoryItems.html', items=items)


@app.route('/catalog/<string:categoryName>/<string:itemName>')
def itemPage(categoryName, itemName):
    description = str(session.query(Item.description).filter_by(category=categoryName, name=itemName).one())[3:-3]
    return render_template('item.html', description=description)


@app.route('/catalog/add', methods=['GET', 'POST'])
def addPage():
    if (request.method == 'POST'):
        newItem = Item(name=request.form['name'], category=request.form['category'],
                       description=request.form['description'])
        session.add(newItem)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('addItem.html')


@app.route('/catalog/<string:itemName>/edit', methods=['GET', 'POST'])
def editPage(itemName):
    if (request.method == 'POST'):
        item = session.query(Item).filter_by(name=itemName).one()
        item.name = request.form['name']
        item.category = request.form['category']
        item.description = request.form['description']
        session.add(item)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('editItem.html')


@app.route('/catalog/<string:itemName>/delete', methods=['GET', 'POST'])
def deletePage(itemName):
    if (request.method == 'POST'):
        item = session.query(Item).filter_by(name=itemName).one()
        session.delete(item)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('deleteItem.html')


@app.route('/catalog.json')
def json():
    items = session.query(Item).all()
    return jsonify(items=[i.serialize for i in items])


@app.route('/catalog/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form['email'])
        newUser = User(email=request.form['email'], name=request.form['name'], password=request.form['password'])
        session.add(newUser)
        session.commit()
        return redirect('/', code=302)
    else:
        return render_template('registerUser.html')


@app.route('/catalog/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginUser = session.query(User).filter_by(email=request.form['email'], password=request.form['password'])
        if (loginUser):
            return redirect('/', code=302)
    else:
        return render_template('loginUser.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

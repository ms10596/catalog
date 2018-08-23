from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item
app = Flask(__name__)

engine = create_engine('sqlite:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def homepage():
    categories = session.query(Item.category).distinct()
    output = ''
    for category in categories:
        output += str(category)[3:-3]
        output += '</br>'

    movies = session.query(Item).order_by(Item.id.desc()).all()
    for movie in movies:
        output += str(movie.name)
        output += '('
        output += str(movie.category)
        output += ')</br>'
    return output

@app.route('/catalog/<string:categoryName>/items')
def categoryPage(categoryName):
    items = session.query(Item.name).filter_by(category = categoryName)
    output = ''
    for item in items:
        output += str(item)[3:-3]
        output += '</br>'
    return output
@app.route('/catalog/<string:categoryName>/<string:itemName>')
def itemPage(categoryName, itemName):
    description = str(session.query(Item.description).filter_by(category=categoryName, name=itemName).one())[3:-3]
    return description
@app.route('/catalog/add', methods=['GET', 'POST'])
def addPage():
    if(request.method == 'POST'):
        newItem = Item(name=request.form['name'], category=request.form['category'], description=request.form['description'])
        session.add(newItem)
        session.commit()
    else:
        return "page to create new Item"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)

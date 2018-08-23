from flask import Flask
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

    movies = session.query(Item.name).order_by(Item.id.desc())
    for movie in movies:
        output += str(movie)[3:-3]
        output += '</br>'
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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)

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
    items = session.query(Item).all()
    print (items)
    output = ''
    for item in items:
        output += item.category
        output += '</br>'
    return output



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)

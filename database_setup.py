#!/usr/bin/python

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text

engine = create_engine('sqlite:////var/www/catalog/catalog.db')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True)
    name = Column(Text)
    password = Column(Text)

    @property
    def serialize(self):
        return {
            'email': self.email,
            'name': self.name,
            'password': self.password,
        }


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    name = Column(Text)
    categoryId = Column(Integer, ForeignKey('category.id'))
    description = Column(Text)
    user = relationship(User)
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'category': self.category.serialize,
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


Base.metadata.create_all(engine)

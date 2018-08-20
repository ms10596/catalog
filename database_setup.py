#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///catalog')

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    email = Column(String, primary_key=True)
    name = Column(String)
    password = Column(String)

    # @property
    # def serialize(self):
    #     return {
    #         'email' : self.email,
    #         'name' : self.name,
    #         'password' : self.password,
    #     }


class Item(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)

    # @property
    # def serialize(self):
    #     return {
    #         'id' : self.id,
    #         'name' : self.name,
    #         'category' : self.category,
    #         'description' : self.description
    #     }


Base.metadata.create_all(engine)

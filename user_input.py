#!bin/bash/env python3
import sqlite3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'userInfo'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    password = Column(String(8), nullable=False)

class URLInfo(Base):
    __tablename__ = 'urlInfo'
    id = Column(Integer, primary_key=True)
    original_URL = Column(String(100))
    shortened_URL = Column(String(100))
    generic_counter = Column(Integer,default=0)
    twitter_counter = Column(Integer,default=0)
    reddit_counter = Column(Integer,default=0)

user_name = input('Enter a username:')
user_password = input('Enter password for {} :'.format(user_name))

print (user_name,user_password)

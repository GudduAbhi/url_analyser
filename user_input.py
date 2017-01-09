#!bin/bash/env python3
import sqlite3
import base62encoder
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker,backref
from sqlalchemy import create_engine

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'userInfo'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250))
    password = Column(String(8), nullable=False)
    url_info = relationship('URLInfo', secondary='user_url_info')

class URLInfo(Base):
    __tablename__ = 'urlInfo'
    url_id = Column(Integer, primary_key=True)
    original_URL = Column(String(100))
    shortened_URL = Column(String(100),default='')
    generic_counter = Column(Integer,default=0)
    twitter_counter = Column(Integer,default=0)
    reddit_counter = Column(Integer,default=0)
    user_info = relationship('UserInfo',secondary='user_url_info')

class UserURLInfo(Base):
    __tablename__ = 'user_url_info'
    user_id = Column(Integer, ForeignKey('userInfo.user_id'), primary_key=True)
    url_id = Column(Integer, ForeignKey('urlInfo.url_id'), primary_key=True)

if __name__ == "__main__":
    session = sessionmaker()
    engine = create_engine('sqlite:///')
    session.configure(bind=engine)
    Base.metadata.create_all(engine)

    user_name = input('Enter a username:')
    user_password = input('Enter password for {} :'.format(user_name))
    user_url = input('Enter URL to shorten:')

    s = session()
    a_user = UserInfo(name=user_name,password=user_password)
    a_url = URLInfo(original_URL=user_url)
    s.add(a_user)
    s.add(a_url)
    s.commit()
    print (a_user.user_id,a_url.url_id)
    print('URLInfo====>',a_url.url_id)
    s.close()

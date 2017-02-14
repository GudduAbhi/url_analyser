import sqlite3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#session = sessionmaker()
#engine = create_engine('sqlite:////home/abhishek/git/url_analyzer/test.sqlite')
#session.configure(bind=engine)
Base = declarative_base()
#Base.metadata.create_all(engine)



class UserInfo(Base):
    __tablename__ = 'userInfo'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250))
    #password = Column(String(8), nullable=False)
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

def start_db():
    session = sessionmaker()
    engine = create_engine('sqlite:////home/abhishek/git/url_analyzer/test.db')
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return session

#!bin/bash/env python3
import sqlite3
from db_schema import UserInfo,URLInfo,UserURLInfo,start_db
import base62encoder
import http_handler
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


#Base = declarative_base()

if __name__ == "__main__":
    #engine = create_engine('sqlite:///test.db')
    session = http_handler.start_db()
    short_url = ''
    user_name = input('Enter a username:')
    user_url = input('Enter URL to shorten:')
    s = session()
    one_more = register_info_into_db(s,user_name,user_url)
    while one_more.lower() != 'no':
        if one_more.lower() == 'yes':
            user_name = input('Enter a username:')
            user_url = input('Enter URL to shorten:')
            http_handler.register_info_into_db(s,user_name,user_url)
        else:
            print('Exiting...')
            break
    s.close()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys


from sqlalchemy import create_engine
CURRENT_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

sys.path.append(CURRENT_DIR)
sys.path.append(APPLICATION_DIR)
from models import Protocol, Base

db_connection = configuration.get('database')

username = db_connection.get('username')
password = db_connection.get('password')
host = db_connection.get('host')
db_name = db_connection.get('db_name')

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}".format(username, password, host, db_name)

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys


from sqlalchemy import create_engine
CURRENT_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

sys.path.append(CURRENT_DIR)
sys.path.append(APPLICATION_DIR)
from models import Protocol, Base
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://frickel:frickel@178.254.54.45:3306/poller'

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
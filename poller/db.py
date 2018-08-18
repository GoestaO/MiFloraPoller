from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration import configuration
db_connection = configuration.get('database')

username = db_connection.get('username')
password = db_connection.get('password')
db_name = db_connection.get('db_name')

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}".format(username, password, db_name)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()
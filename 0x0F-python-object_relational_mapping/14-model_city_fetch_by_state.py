#!/usr/bin/python3
"""Lists all City objects from the database `hbtn_0e_14_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    _, user, passwd, database = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name).join(State)

    for state, id, name in result.order_by(City.id):
        print("{}: ({}) {}".format(state, id, name))

    session.close()

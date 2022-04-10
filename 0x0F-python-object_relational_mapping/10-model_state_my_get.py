#!/usr/bin/python3
"""Prints the State object with the name passed as argument
   from the database `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
import sys

if __name__ == '__main__':
    _, user, passwd, database, state = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    flag = 0
    result = session.query(State)

    for log in result.order_by(State.id):
        if log.name == state:
            print(log.id)
            flag = 1
    if flag == 0:
        print("Not found")

    session.close()

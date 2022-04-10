#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
import sys

if __name__ == '__main__':
    _, user, passwd, database = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(user, passwd, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()

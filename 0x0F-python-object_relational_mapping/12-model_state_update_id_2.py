#!/usr/bin/python3
"""Changes the name of a State object from the database `hbtn_0e_6_usa`
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

    state = session.query(State).get(2)
    state.name = "New Mexico"

    session.add(state)
    session.commit()
    session.close()

#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'
   from the database `hbtn_0e_6_usa`
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

    result = session.query(State).filter(State.name.like("%a%"))
    deleted = result.delete(synchronize_session='fetch')

    session.commit()
    session.close()

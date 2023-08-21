#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def search_user_input:
    """ function to search input given bby user"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.id).filter(State.name == sys.argv[4]).first()
    if query is None:
        print('Not found')
    else:
        print(query[0])


if __name__ == '__main__':
    search_user_input()

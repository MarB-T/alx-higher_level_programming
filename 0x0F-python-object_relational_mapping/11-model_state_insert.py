#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def insert():
    """function to insert into a table"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)


if __name__ == '__main__':
    insert()

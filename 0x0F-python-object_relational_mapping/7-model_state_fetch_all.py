#!/usr/bin/python3
"""
Fetches all from state
"""

from sys import argv
from sqlalchemy import Integer, Column, String
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def fetch_all():
    """function to fetch all from a model"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    fetch_all()

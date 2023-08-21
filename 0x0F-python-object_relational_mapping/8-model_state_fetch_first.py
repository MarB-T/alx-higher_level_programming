#!/usr/bin/python3
"""
Fetches the first instance in states
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Integer, String, Column


def fetch_first():
    """
    function to fetch the first row in states
    """
    db_url = ('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print()

    session.close()


if __name__ == '__main__':
    fetch_first()

#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def delete_all():
    """ function to delete everything in a table"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).all()
    for st in state:
        session.delete(st)
    session.commit()


if __name__ == "__main__":
    delete_all()

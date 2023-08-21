#!/usr/bin/python3
"""
script that lists all states having letter 'a'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def states_with_a():
    """ function to fetch states containing letter 'a' """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],
                                   argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(
            State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    states_with_a()

#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City


def fetch_by_state():
    """function to fetch cities by state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State)\
                   .filter(City.state_id == State.id)\
                   .order_by(City.id)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == '__main__':
    fetch_by_state()

#!/usr/bin/python3
"""
first python script using sqlalchemy
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class States(Base):
    """ defines a table states """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql://root:root@localhost:3306')

Base.metadata.create_all(engine)

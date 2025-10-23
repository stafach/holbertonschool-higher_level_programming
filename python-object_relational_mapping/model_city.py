#!/usr/bin/python3
"""
Contains the class definition of a
City and inherit from Base imported
from model_state
"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from model_state import Base, State


class City(Base):
    """
    State class that maps to the MySQL table 'cities'
    inherit from Base imported from model_state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

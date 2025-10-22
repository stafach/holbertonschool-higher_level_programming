#!/usr/bin/python3
"""
Contains the class definition of a
State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that maps to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://USERNAME:PASSWORD@localhost:3306/DATABASE_NAME'
        )

    Base.metadata.create_all(engine)

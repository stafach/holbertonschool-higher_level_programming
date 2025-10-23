#!/usr/bin/python3
"""
script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import pymysql

pymysql.install_as_MySQLdb()

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana = State(name="Louisiana")
    session.add(Louisiana)

    state = session.query(State).filter(State.name == "Louisiana").first()

    print("{}".format(state.id))
    session.commit()
    session.close()

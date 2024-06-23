#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id = 2
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


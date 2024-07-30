#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>")
        exit(1)

    username, password, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(f"{state.id}")
        else:
            print("Not found")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()


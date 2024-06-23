#!/usr/bin/python3
"""
This script lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>")
        exit(1)

    # Construct the database URL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create the engine and session
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the database for states containing 'a' and sort by id
        states = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()
        if states:
            for state in states:
                print('{}: {}'.format(state.id, state.name))
        else:
            print("No state contains the letter 'a'")
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        session.close()


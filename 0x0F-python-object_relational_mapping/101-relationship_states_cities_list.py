#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects,
contained in the database `hbtn_0e_101_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and list all states with their cities.
    """

    # Database connection parameters
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create engine and bind session
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and their cities
    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    # Print results in the required format
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Close session
    session.close()


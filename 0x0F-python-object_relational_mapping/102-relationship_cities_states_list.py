#!/usr/bin/python3
"""
This script lists all City objects from the database `hbtn_0e_101_usa`,
along with their associated State names.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and list all cities with their associated states.
    """

    # Database connection parameters
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create engine and bind session
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their associated states
    cities = session.query(City).order_by(City.id).all()

    # Print results in the required format
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()


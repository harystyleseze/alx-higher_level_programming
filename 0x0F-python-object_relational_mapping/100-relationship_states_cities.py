#!/usr/bin/python3
"""
This script creates the State "California" and City "San Francisco"
and links them via SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # MySQL connection URL
    db_uri = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    
    # Create engine and bind session
    engine = create_engine(db_uri, echo=True)  # Set echo=True to see SQL commands executed
    Base.metadata.create_all(engine)  # Create all tables defined in Base

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State "California" and City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add city to state's cities collection
    california.cities.append(san_francisco)

    # Add state to session and commit
    session.add(california)
    session.commit()

    # Print the id of the newly created City object
    print(san_francisco.id)

    session.close()


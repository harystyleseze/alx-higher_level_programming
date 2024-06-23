#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    # Check if all 3 arguments are passed
    if len(argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    try:
        # Connect to MySQL database
        db_connect = db.connect(host="localhost", port=3306,
                                user=username, passwd=password, db=database)

        with db_connect.cursor() as db_cursor:
            # Execute SQL query to fetch cities with their respective states
            db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                    FROM cities JOIN states ON cities.state_id \
                                    = states.id ORDER BY cities.id ASC")
            rows_selected = db_cursor.fetchall()

            # Output each row
            for row in rows_selected:
                print(row)

    except db.Error as e:
        print(f"Error connecting to MySQL database: {e}")
    finally:
        if db_connect:
            db_connect.close()


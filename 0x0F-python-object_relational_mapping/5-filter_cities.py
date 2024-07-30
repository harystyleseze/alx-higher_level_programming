#!/usr/bin/python3
"""
This script lists all cities of a given state
from the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    of the given state.
    """

    # Connect to the database
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        # Use a parameterized query to prevent SQL injection
        query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """
        db_cursor.execute(query, (argv[4],))
        rows_selected = db_cursor.fetchall()

    # Print the results
    if rows_selected:
        print(", ".join([row[0] for row in rows_selected]))
    else:
        print("")


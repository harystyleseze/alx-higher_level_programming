#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states
    from the database, sorted by id.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    db_cursor = db_connect.cursor()

    # Execute the SQL query with ORDER BY to sort by id in ascending order
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the executed query
    rows_selected = db_cursor.fetchall()

    # Print each row
    for row in rows_selected:
        print(row)

    # Close the cursor and connection
    db_cursor.close()
    db_connect.close()


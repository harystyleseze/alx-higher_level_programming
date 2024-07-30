#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states that match the user input.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    db_cursor = db_connect.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    db_cursor.execute(query)

    # Fetch all the rows from the executed query
    rows_selected = db_cursor.fetchall()

    # Print each row
    for row in rows_selected:
        print(row)

    # Close the cursor and connection
    db_cursor.close()
    db_connect.close()


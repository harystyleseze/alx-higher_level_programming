#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        exit(1)

    try:
        # Establish database connection
        db_connect = db.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])

        # Create a cursor object
        db_cursor = db_connect.cursor()

        # Construct parameterized SQL query
        query = "SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY id ASC"
        params = {'name': argv[4]}

        # Execute SQL query with parameters
        db_cursor.execute(query, params)

        # Fetch and display results
        rows_selected = db_cursor.fetchall()
        for row in rows_selected:
            print(row)

    except db.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if db_cursor:
            db_cursor.close()
        if db_connect:
            db_connect.close()


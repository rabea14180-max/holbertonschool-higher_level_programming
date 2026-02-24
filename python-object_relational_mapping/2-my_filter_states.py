#!/usr/bin/python3
"""
Displays all values in the states table
where name matches the given argument
Usage:
./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Create query using format (as required)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
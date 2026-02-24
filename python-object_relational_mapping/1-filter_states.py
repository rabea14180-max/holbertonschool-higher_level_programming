#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (upper N)
from the specified MySQL database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create cursor
    cur = db.cursor()

    # Execute query
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch and display results
    for row in cur.fetchall():
        print(row)

    # Close connections
    cur.close()
    db.close()
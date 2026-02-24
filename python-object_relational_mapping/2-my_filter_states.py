#!/usr/bin/python3
"""
This module filters states by name from a MySQL database.

It connects to a MySQL server running on localhost at port 3306,
queries the states table, and displays rows where the name matches
the provided argument. Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves states
    that match the provided name argument.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
    
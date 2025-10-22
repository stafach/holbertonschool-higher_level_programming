#!/usr/bin/python3
"""
script that lists all states with a name starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * "
        "FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY states.id"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
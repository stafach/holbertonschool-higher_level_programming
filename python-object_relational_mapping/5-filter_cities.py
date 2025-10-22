#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
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
        "SELECT cities.name "
        "FROM cities "
        "LEFT JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],))

    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()

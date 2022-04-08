#!/usr/bin/python3
"""This module connect to a MySQL server and takes in the name of a state
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    _, user, passwd, db, state = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=passwd,
                         db=db)
    cur = db.cursor()
    sql = "SELECT\
                cities.name\
           FROM\
                cities\
           INNER JOIN\
                states ON cities.state_id = states.id\
           WHERE\
                states.name = %s\
           ORDER BY cities.id ASC"

    cur.execute(sql, (state,))
    logs = cur.fetchall()
    cities = []
    for log in logs:
        cities.append(log[0])

    print(", ".join(cities))

    cur.close()
    db.close()

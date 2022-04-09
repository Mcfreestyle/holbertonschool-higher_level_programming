#!/usr/bin/python3
"""This module connect to a MySQL server and lists all states
    with a name starting with N from the database `hbtn_0e_0_usa`
"""
import MySQLdb
import sys


if __name__ == "__main__":
    _, user, passwd, db = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=passwd,
                         db=db)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

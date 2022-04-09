#!/usr/bin/python3
"""This module connect to a MySQL server, takes in an argument
    and displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
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

    sql = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cur.execute(sql.format(state))
    logs = cur.fetchall()
    for log in logs:
        print(log)

    cur.close()
    db.close()

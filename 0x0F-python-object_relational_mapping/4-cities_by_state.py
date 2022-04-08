#!/usr/bin/python3
"""This module connect to a MySQL server and lists all cities
    from the database `hbtn_0e_4_usa`
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
    sql = "SELECT\
                cities.id,\
                cities.name,\
                states.name\
           FROM\
                cities\
           INNER JOIN\
                states ON cities.state_id = states.id\
           ORDER BY cities.id ASC"

    cur.execute(sql)
    logs = cur.fetchall()
    for log in logs:
        print(log)

    cur.close()
    db.close()

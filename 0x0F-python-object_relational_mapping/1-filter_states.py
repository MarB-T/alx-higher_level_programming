#!/usr/bin/python3
"""
Script to query a database and filter the result
"""
import MySQLdb
import sys


def states_N():
    """function to get states that start with 'N'"""
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", user=uname,
                           passwd=pword, db=dbname, port='3306')
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)

    conn.close()


if __name__ == '__main__':
    states_N()

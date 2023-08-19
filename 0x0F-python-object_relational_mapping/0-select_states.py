#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


def get_states():
    """ function to get states of a given database """
    uname = sys.argv[1]
    pword = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=uname, passwd=pword, db=dbname)
    cur = db.cursor()

    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print("{}, '{}'".format(state[0], state[1]))

    db.close()


if __name__ == '__main__':
    get_states()

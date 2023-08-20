#!/usr/bin/python3
""" Script to use user input argument to filter results """
import MySQLdb
from sys import argv


def get_state():
    """ Function to get state given by user """
    conn = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=argv[1],
                    passwd=argv[2],
                    db=argv[3])
    cur = conn.cursor()
    query = ("SELECT * FROM states
             WHERE name='{}'
             ORDER BY id ASC".format(argv[4]))
    cur.execute(query)
    state = cur.fetchall()
    print(state)
    conn.close


if __name__ == '__main__':
    get_state()

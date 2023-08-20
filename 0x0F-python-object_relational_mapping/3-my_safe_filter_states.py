#!/usr/bin/python3
"""
Script to use user input argument to filter results
safely against sql injection
"""
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    search = (argv[4],)
    cur.execute(query, search)
    states = cur.fetchall()
    for state in states:
        print(state)
    conn.close()


if __name__ == '__main__':
    get_state()

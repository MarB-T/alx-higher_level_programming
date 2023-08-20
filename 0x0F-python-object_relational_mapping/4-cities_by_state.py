#!/usr/bin/python3
"""
script that fetches from two tables using JOIN
"""
import MySQLdb
from sys import argv


def cities_by_state():
    """ Function to get cities by states """
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id")
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()


if __name__ == '__main__':
    cities_by_state()

#!/usr/bin/python3
"""
script to get all the cities in a given state
"""
import MySQLdb
from sys import argv


def all_cities_in_state():
    """
    function to get all the cities in a given state
    """
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %(name)s "
             "ORDER BY cities.id")
    search_state = {'name': argv[4]}
    cur.execute(query, search_state)
    cities = cur.fetchall()

    citis = []
    for city in cities:
        citis.append(city[0])

    citis_str = ', '.join(citis)
    print(citis_str)

    cur.close()


if __name__ == '__main__':
    all_cities_in_state()

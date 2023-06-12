#!/usr/bin/python3
""" not in any module defined """


class MyList(list):
    """ class MyList inherits from list """

    def print_sorted(self):
        """ prints the list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)

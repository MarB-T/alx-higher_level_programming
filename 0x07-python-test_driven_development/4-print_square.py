#!/usr/bin/python3
"""
Prints square using '#'
"""

def print_square(size):
    """
    function to print square of given size

    Args:
        size: size of square

    Raises:
        TypeError: when size is not a valid integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

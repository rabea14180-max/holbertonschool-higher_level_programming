#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds two integers
"""
def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    a and b must be integers or floats, otherwise a TypeError is raised.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

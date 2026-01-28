#!/usr/bin/python3
"""
Defines a BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def integer_validator(self, name, value):
        """Validates value as a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

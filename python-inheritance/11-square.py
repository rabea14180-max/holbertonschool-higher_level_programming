#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle's __init__ with width and height equal to size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description [Square] <width>/<height>"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)

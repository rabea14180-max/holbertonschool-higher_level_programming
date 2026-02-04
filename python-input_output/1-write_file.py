#!/usr/bin/python3
"""
Docstring for python-input_output.1-write_file
"""


def write_file(filename="", text=""):
    """
        Docstring for write_file
        write a text
        :param filename: Description
        :param text: Description
        """

    with open(filename, 'w', encoding='utf-8') as file:
        writee = file.write(text)
    return writee

#!/usr/bin/python3
"""
Docstring for python-input_output.2-append_write
"""


def append_write(filename="", text=""):
    """
        Docstring for append_write
        write a text
        :param filename: Description
        :param text: Description
        """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

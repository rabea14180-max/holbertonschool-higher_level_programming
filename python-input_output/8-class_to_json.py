#!/usr/bin/python3
"""Module for converting an object to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object."""
    return obj.__dict__

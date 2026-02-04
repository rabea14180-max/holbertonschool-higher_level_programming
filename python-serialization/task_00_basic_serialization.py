#!/usr/bin/python3
"""Basic serialization module: serialize and deserialize Python dictionaries
to and from JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON file path.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): JSON file path to read from.

    Returns:
        dict: Python dictionary loaded from JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

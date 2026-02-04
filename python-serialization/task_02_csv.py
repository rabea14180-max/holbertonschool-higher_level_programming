#!/usr/bin/python3
"""Module to convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into a JSON file named 'data.json'.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Read CSV file using DictReader
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False

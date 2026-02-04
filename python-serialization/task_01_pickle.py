#!/usr/bin/python3
"""Module for serializing and deserializing a custom Python object using pickle."""

import pickle


class CustomObject:
    """Custom object with attributes: name, age, is_student."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the given filename.

        If an error occurs (file permission, etc.), silently return None.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return a CustomObject instance from the given filename.

        Returns None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None

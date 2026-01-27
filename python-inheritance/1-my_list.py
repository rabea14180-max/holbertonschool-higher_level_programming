#!/usr/bin/python3
class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending) without modifying the original list"""
        print(sorted(self))

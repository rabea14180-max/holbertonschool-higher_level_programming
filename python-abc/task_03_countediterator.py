#!/usr/bin/env python3
"""
CountedIterator: wraps a Python iterator and keeps track of the number of items iterated.
"""


class CountedIterator:
    """Iterator wrapper that counts the number of items fetched"""

    def __init__(self, iterable):
        """Initialize with an iterable"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return self as iterator"""
        return self

    def __next__(self):
        """Fetch the next item, increment counter"""
        item = next(self.iterator)  # May raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far"""
        return self.count

#!/usr/bin/env python3
"""
Demonstrates mixins: Dragon can swim and fly using SwimMixin and FlyMixin.
"""


class SwimMixin:
    """Mixin that adds swimming capability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly"""

    def roar(self):
        print("The dragon roars!")

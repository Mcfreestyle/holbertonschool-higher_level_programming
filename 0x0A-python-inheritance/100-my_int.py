#!/usr/bin/python3
"""This module supplies the ``MyInt`` class
"""


class MyInt(int):
    """Definition of the class"""

    def __eq__(self, other):
        """Override equal through not equal"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """Override not equal through equal"""
        return (super().__eq__(other))

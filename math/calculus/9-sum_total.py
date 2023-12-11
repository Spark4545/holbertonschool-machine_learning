#!/usr/bin/env python3
"""
    Module to calculate a sum
"""


def summation_i_squared(n):
    """Function to calculate a sum"""
    if (type(n) is not int) or (n is None) or (n < 1):
        return None
    else:
        numbers = range(1, n+1)
        result = 0
        result = map(lambda i: i ** 2, numbers)
        return sum(result)

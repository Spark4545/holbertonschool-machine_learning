#!/usr/bin/env python3
"""
    Module to calculate the dimensions of a matrix
"""


def matrix_shape(matrix):
    """Function that will calculate the dimensions of a matrix"""
    if type(matrix[0]) != list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])

#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, returns a new matrix.
    matrix: list of lists of integers/floats
    div: int or float, cannot be zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix

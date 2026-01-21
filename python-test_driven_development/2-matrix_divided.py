#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows of matrix are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is equal to 0

    Returns:
        list of lists: new matrix with divided values rounded to 2 decimals
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

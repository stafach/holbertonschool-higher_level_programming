#!/usr/bin/python3
"""
This module defines a function divide a matrix
It checks that the input is a list of list of integers/floats,
if the len of all list are the same
and if the divide number is an integer or float and not 0
Return a new matrix with the divid number
"""


def matrix_divided(matrix, div):
    """Divide a matrix by a given number

    Args:
        matrix (list): the list of list
        div (int, float): the divide number

    Raises:
        TypeError: If divide number is not float or integer
        ZeroDivisionError: If divide number is 0
        TypeError: If matrix is not a list of list of integer or float
        TypeError: If len of each list is different
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (
         not isinstance(matrix, list)
         or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    new = []
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            new_row.append(round(value / div, 2))
        new.append(new_row)
    return new

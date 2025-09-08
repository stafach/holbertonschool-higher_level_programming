#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [row.copy() for row in matrix]
    for i, row in enumerate(new):
        for j, value in enumerate(row):
            new[i][j] = value ** 2
    return new

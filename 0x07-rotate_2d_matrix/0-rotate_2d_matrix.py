#!/usr/bin/python3
"""
    Given an n x n 2D matrix, rotate it 90
    degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
        Arg:
            matrix: an n x n 2D matrix
            return: transpose of matrix (edited in place)
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

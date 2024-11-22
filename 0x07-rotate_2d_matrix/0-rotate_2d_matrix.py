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
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

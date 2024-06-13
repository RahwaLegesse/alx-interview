#!/usr/bin/python3
"""Module Matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates matrix 2.

    Parameters:
        matrix (list[list[int]]): the 2D matrix

    Returns:
        None
    """
    # First, we reverse the order of the rows
    matrix.reverse()
    # Next, we swap the elements in the diagonal only once
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

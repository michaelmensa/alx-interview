#!/usr/bin/python3
'''
Module 0-rotate_2d_matrix.py Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    ''' function to rotate 2D matrix 90 degrees
    clockwise '''
    # transpose matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse transposed matrix
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            matrix[j][i], matrix[j][N - 1 - i] = (matrix[j][N - 1 - i],
                                                  matrix[j][i])

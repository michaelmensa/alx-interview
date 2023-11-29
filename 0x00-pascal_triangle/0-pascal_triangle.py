#!/usr/bin/python3
'''
Module - Pascal's triangle by Michael Mensah
'''


def pascal_triangle(n):
    '''
    prints pascal triangle
    args: n
    returns empty list when n is less than or equals zero
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

#!/usr/bin/python3
'''
Module: ALX interview question. Minimum Operations
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n):
    '''
    method that calculates the fewest number of operations needed to result
    in exactly n H characters in a file.

    Params: n

    Returns an integer.
    If n is impossible to achieve, return 0
    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)
        if dp[i] == float('inf'):
            dp[i] = i

    return dp[n] if dp[n] != float('inf') else 0
    '''
    operations = 0
    for _ in range(2, int(n**0.5) + 1):
        while n % _ == 0:
            operations += _
            n //= _

    if n > 1:
        operations += n

    return operations

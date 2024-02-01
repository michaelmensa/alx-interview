#!/usr/bin/python3
'''
Module: 0-making_change.py
'''


def makeChange(coins, total):
    ''' function that determines the fewest number of
    coins needed to meet a given amount total
    '''
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for coin in coins:
            if t - coin >= 0:
                dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1

#!/usr/bin/python3

'''
Module: prime game
'''


def isWinner(x, nums):
    ''' main function isWinner '''
    def is_prime(num):
        ''' check if num is prime '''
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(current, remaining):
        ''' get next prime number '''
        for num in remaining:
            if is_prime(num):
                return num
        return None

    def play_game(n):
        ''' plays the game '''
        if n == 1:
            return "Ben"
        turns = 0
        remaining_numbers = list(range(1, n + 1))
        while True:
            prime = get_next_prime(2, remaining_numbers)
            if prime is None:
                break
            turns += 1
            index = 0
            while index < len(remaining_numbers):
                if remaining_numbers[index] % prime == 0:
                    del remaining_numbers[index]
                else:
                    index += 1
        if turns % 2 == 0:
            return 'Ben'
        else:
            return "Maria"

    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = play_game(n)
        wins[winner] += 1

    max_wins = max(wins.values())
    if wins["Maria"] == wins["Ben"]:
        return None
    else:
        return max(wins, key=wins.get)

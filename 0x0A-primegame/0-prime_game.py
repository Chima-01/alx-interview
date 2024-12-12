#!/usr/bin/python3
"""
    using prime numbers, game theory, and
    algorithm optimization to solve a competitive game scenario.
"""


def isWinner(x, nums):
    """
        Args:
            x: number of game rounds
            num: An array of number to find prime within
    """
    if x <= 0 or not nums:
        return None

    players = {
            'Maria': 0,
            'Ben': 0
            }

    for i in range(x):
        if nums[i] <= 1:
            players["Ben"] += 1
            continue

        index = [False, False] + [True] * (nums[i] - 1)

        p = 2
        while (p * p <= nums[i]):
            if index[p] is True:
                for j in range(p * p, nums[i] + 1, p):
                    index[j] = False

            p += 1

        true_count = index.count(True)

        if true_count % 2:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    return 'Maria' if players['Maria'] > players['Ben'] else 'Ben'

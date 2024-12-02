#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
        Args:
            coins: a list of coin for change
            total: total amount to make a round up change with
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    total_cpy = total
    count = 0

    for coin in coins:
        while total_cpy >= coin:
            total_cpy -= coin
            count += 1
        if total_cpy == 0:
            break

    return count if total_cpy == 0 else -1

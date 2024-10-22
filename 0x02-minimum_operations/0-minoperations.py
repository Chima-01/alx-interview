#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Arg:
        n: number given to calculate
        the trivk is to add the number prime factors
    """
    if n <= 1:
        return 0

    total_factor = 0
    factor = 2
    num = n

    while factor * factor <= num:
        if num % factor:
            factor += 1
        else:
            total_factor += factor
            num //= factor

    if n == num:
        return num

    if num > 1:
        total_factor += num
    return total_factor

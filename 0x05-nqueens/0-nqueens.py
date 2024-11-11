#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


def nqueens(N):
    """
    gets n arg if queen
    creates an N X N list
    """
    board = [["." for _ in range(N)] for _ in range(N)]


if __name__ == "__main__":
    from sys import argv
    from sys import exit

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(N)

#!/usr/bin/python3
"""
In this project I'll be calculating
the perimeter of the island described in grid
all 1's surronded by number of 0's represent length of 1
for instance a 1 surrounded by 4 0's is = 4 in length
"""


def island_perimeter(grid):
    """
        arg:
            grid: a list of list (represents the island)
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter

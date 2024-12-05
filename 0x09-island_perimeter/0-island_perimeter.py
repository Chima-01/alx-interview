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
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if col != 0:
                    if grid[row][col - 1] == 0:
                        perimeter += 1
                try:
                    if grid[row][col + 1] == 0:
                        perimeter += 1
                except IndexError:
                    pass
                if row != 0:
                    if grid[row - 1][col] == 0:
                        perimeter += 1
                try:
                    if grid[row + 1][col] == 0:
                        perimeter += 1
                except IndexError:
                    pass

    return perimeter

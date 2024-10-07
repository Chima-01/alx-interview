"""
create a pascal triangle using python
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    pascal_triangle = []

    for i in range(n):
        numbers = []
        for x in range(i + 1):
            if x == 0 or x == i:
                numbers.append(1)
            else:
                current_row = pascal_triangle[i - 1]
                numbers.append(current_row[x - 1] + current_row[x])
        pascal_triangle.append(numbers)

    return pascal_triangle
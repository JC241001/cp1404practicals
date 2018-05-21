"""
CP1404/CP5632 Practical
Recursion from scratch
"""


def pyramid_blocks_loop(rows):
    """Calculate number of blocks using loop"""
    sum_blocks = 0
    for index in range(1, rows+1):
        sum_blocks = sum_blocks + index
    return sum_blocks


print('LOOPING')
for i in range(1, 7):
    print('{} blocks required for {} rows'.format(pyramid_blocks_loop(i), i))
print()


def pyramid_blocks_recursion(rows):
    """Calculate number of blocks using recursion"""
    # Base Case
    if rows == 0:
        return 0

    # Recursive case
    return rows + pyramid_blocks_recursion(rows - 1)

print('RECURSING')
for i in range(1, 7):
    print('{} blocks required for {} rows'.format(pyramid_blocks_recursion(i), i))
print()

"""
CP1404/CP5632 Practical
Recursion from scratch
"""


def pyramid_blocks_loop(rows):
    sum = 0
    for i in range(1, rows+1):
        sum = sum + i
    return sum


print('LOOPING')
for i in range(1, 7):
    print('{} blocks required for {} rows'.format(pyramid_blocks_loop(i), i))
print()


def pyramid_blocks_recursion(rows):
    # Base Case
    if rows == 0:
        return 0

    # Recursive case
    return rows + pyramid_blocks_recursion(rows - 1)

print('RECURSING')
for i in range(1, 7):
    print('{} blocks required for {} rows'.format(pyramid_blocks_recursion(i), i))
print()

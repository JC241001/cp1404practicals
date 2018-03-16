"""Lottery ticket generator"""

import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    for i in range(get_num_picks()):
        pick_list = []
        for j in range(NUMBERS_PER_LINE):
            pick_list.append(get_number(pick_list))
        pick_list.sort()
        [print("{:3}".format(number), end=' ') for number in pick_list]
        print()


def get_num_picks():
    valid_input = False
    while not valid_input:
        try:
            result = int(input("How many quick picks? "))
            valid_input = True
        except ValueError:
            print("Please provide integer")

    return result


def get_number(a_list):
    unique_num = random.randint(MIN, MAX)
    while unique_num in a_list:
        unique_num = random.randint(MIN, MAX)

    return unique_num


if __name__ == '__main__':
    main()

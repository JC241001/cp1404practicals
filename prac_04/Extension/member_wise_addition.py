"""Performs member wise addition of lists of numbers"""


def member_wise_addition(list_1, list_2):

    result = []
    size = min([len(list_1), len(list_2)])

    # add up to smaller list
    for index in range(size):
        result.append(list_1[index] + list_2[index])

    # add rest of bigger list
    if size == len(list_1):
        for k in range(len(list_2) - size):
            result.append(list_2[k + size])
    else:
        for k in range(len(list_1) - size):
            result.append(list_1[k + size])

    return result


def main():
    a = [1, 3]
    b = [1]
    c = []
    d = [4, 4, 4, 4, 5]
    e = [1, 1, 1, 1, 4]
    f = list(range(12))
    master_list = [a, b, c, d, e, f]
    for i in master_list:
        for j in master_list:
            print(member_wise_addition(i, j))


main()



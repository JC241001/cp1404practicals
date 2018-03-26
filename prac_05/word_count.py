"""
CP1404/CP5632 Practical
Counts the number of a particular word in a string
"""

INITIAL = 0


def main():
    string_list = input("Text: ").split()

    string_list = [string_list[i].strip(',.;()[]') for i in range(len(string_list))]

    word_to_count = {}
    for word in string_list:
        if word not in word_to_count:
            word_to_count[word] = 1
        else:
            word_to_count[word] += 1
    string_list = set(string_list)
    string_list = list(string_list)
    string_list = sorted(string_list)
    for word in string_list:
        print('{:{}} : {} '.format(word, get_max_length(string_list), word_to_count[word]))


def get_max_length(a_list):
    result = len(a_list[INITIAL])
    for i in range(len(a_list)):
        if len(a_list[i]) > result:
            result = len(a_list[i])

    return result


main()

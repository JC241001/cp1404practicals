"""
CP1404/CP5632 Practical
Counts the number of a particular word in a string
"""

string_list = input("Text: ").split()
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
    print(word, ':', word_to_count[word])

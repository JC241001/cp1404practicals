"""
CP1404/CP5632 - Practical
Random word generator - automatically generate word format

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WILDCARDS = "#%*"

print("Word format will be automatically generated, any word between 3 & 7 characters")

num_char = random.randint(3, 7)
word_format = ""
for char in range(num_char):
    word_format += random.choice(CONSONANTS+VOWELS+WILDCARDS)

print("Word format is: {}".format(word_format))
print()

word = ""
for kind in word_format:
    if kind == "#":
        word += random.choice(CONSONANTS)
    elif kind == "%":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(CONSONANTS+VOWELS)
    else:
        word += kind

print(word)

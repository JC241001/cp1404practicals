"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    print("This is a random word generator.")
    input_string = input("Enter your word format with c for consonants and v for vowels: ")
    while not is_valid_format(input_string):
        print("Your input is not valid, only enter lowercase c or lowercase v as a sequence")
        input_string = input("Enter your word format with c for consonants and v for vowels: ")

    random_word = generate_random_word(input_string)
    print(random_word)


def is_valid_format(a_string):
    """check if a_string is only a sequence of c's and v's"""
    valid_letters = ['c', 'v']
    if a_string == "":
        return False
    else:
        for char in a_string:
            if char not in valid_letters:
                return False
    return True


def generate_random_word(cv_string):
    """Only provide sequence of c's and v's.  Returns random word"""
    word = ""
    for speech_sound in cv_string:
        if speech_sound == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    return word


if __name__ == '__main__':
    main()

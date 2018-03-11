
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < password_length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower < num_of_lower or count_upper < num_of_upper or count_digit < num_of_numeric or count_special < num_of_special_char:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


password_length = int(input("Enter min password length: "))
num_of_upper = int(input("Enter number of uppercase: "))
num_of_lower = int(input("Enter number of lowercase: "))
num_of_numeric = int(input("Enter number of numbers: "))
num_of_special_char = int(input("Enter number of special: "))

password = ""

while not is_valid_password(password):
    password += chr(random.randint(33,127))


print(password)



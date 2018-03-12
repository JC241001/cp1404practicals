"""ascii table letters mapped to numbers"""

LOWER = 33
UPPER = 127


def main():
    users_char = input("Enter a character: ")
    print("Tha ASCII code for {} is {}".format(users_char, ord(users_char)))
    users_num = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(users_num, chr(users_num)))


def get_number(lower, upper):
    is_valid = False
    while not is_valid:
        try:
            valid_number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            if not lower <= valid_number <= upper:
                print("Invalid number!")
                continue
            is_valid = True
        except ValueError:
            print("Invalid input")
    return valid_number


if __name__ == '__main__':
    main()




# for i in range(LOWER,UPPER+1):
#     print("{:3} {:>5}".format(i, chr(i)))
#
#
# num_col = int(input("how many columns: "))
# for i in range(num_col):
#     print("{:5}".format(i+1), end="")
# print()
#
# for i in range(LOWER, UPPER):
#     for j in range(num_col):
#         print("{:5}".format(i), end="")
#     print()

"""Asks user for name.  Has error checking to ensure name not Blank.
Prints every second letter of provided name"""


def main():
    name = get_name()
    letter_freq = get_letter_freq()
    print_every_nth_letter(name, letter_freq)


def print_every_nth_letter(name, n):
    print("Every 2nd letter is: {}".format(name[::n]))


def get_name():
    name = input("Enter name: ")
    while name == "":
        print("Must enter something")
        name = input("Enter name: ")
    return name


def get_letter_freq():
    valid_integer = False
    while not valid_integer:
        try:
            freq = int(input("Enter letter frequency: "))
            if freq < 1:
                print("Please enter positive integer")
                continue
            valid_integer = True
        except ValueError:
            print("Invalid (not an integer)")
    return freq


if __name__ == '__main__':
    main()

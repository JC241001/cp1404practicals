"""User enters indefinite number of strings, after empty string entered, repeated string is printed"""


def main():
    strings = []
    repeated_strings = []

    string = input("Enter string: ")
    while string != '':
        if string in strings and string not in repeated_strings:
            repeated_strings.append(string)
        strings.append(string)
        string = input("Enter string: ")

    print("Repeated Strings are: ")
    for string in repeated_strings:
        print(string)


if __name__ == '__main__':
    main()

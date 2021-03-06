"""
CP1404/CP5632 - Practical
Pseudo code for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = get_input()
    while choice != "Q":
        if choice == "C":
            process_celsius_to_fahrenheit()
        elif choice == "F":
            process_fahrenheit_to_celsius()
        else:
            print("Invalid option")         # Redundant
        print(MENU)
        choice = get_input()
    print("Thank you.")


def process_fahrenheit_to_celsius():
    valid_input = False
    while not valid_input:
        try:
            fahrenheit = float(input("Fahrenheit: "))
            valid_input = True
        except ValueError:
            print("Please enter a number")
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))


def process_celsius_to_fahrenheit():
    valid_input = False
    while not valid_input:
        try:
            celsius = float(input("Celsius: "))
            valid_input = True
        except ValueError:
            print("Please enter a number")
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def get_input():
    valid_inputs = ["C", "F", "Q"]
    user_choice = input(">>> ").upper()
    while user_choice not in valid_inputs:
        print("Invalid Input\n" + MENU)
        user_choice = input(">>> ").upper()
    return user_choice


if __name__ == '__main__':
    main()


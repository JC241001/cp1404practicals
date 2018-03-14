"""Intermediate exercise with lists of numbers"""


def main():
    numbers = []
    for i in range(5):
        numbers.append(get_number())

    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average of the numbers is: {}".format(sum(numbers)/len(numbers)))


def get_number():
    valid_input = False
    while not valid_input:
        try:
            the_num = int(input("Number: "))
            valid_input = True
        except ValueError:
            print("Integers please!")

    return the_num

if __name__ == '__main__':
    main()

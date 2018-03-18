"""Intermediate exercise with lists of numbers"""


def main():
    numbers = []
    count = 1
    number = get_number(count)
    while number > 0:
        count += 1
        numbers.append(number)
        number = get_number(count)

    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average of the numbers is: {}".format(sum(numbers)/len(numbers)))


def get_number(count):
    valid_input = False
    while not valid_input:
        try:
            the_num = int(input("Number {}: ".format(count)))
            valid_input = True
        except ValueError:
            print("Integers please!")

    return the_num

if __name__ == '__main__':
    main()

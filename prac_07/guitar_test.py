"""CP1404 Practicals - Test guitar class"""


from prac_07.guitar import Guitar


def main():
    guitar_1 = Guitar('Gibson L5', 1922, 16035.40)
    guitar_2 = Guitar('something', 2002, 0.5)

    print(guitar_1)
    print(guitar_2)
    print()

    print('{} get_age() - Expected {}. Got {}'.format(guitar_1.name, 96, guitar_1.get_age()))
    print('{} get_age() - Expected {}. Got {}'.format(guitar_2.name, 16, guitar_2.get_age()))
    print()

    print('{} is_vintage() - Expected {}. Got {}'.format(guitar_1.name, 'True', guitar_1.is_vintage()))
    print('{} is_vintage() - Expected {}. Got {}'.format(guitar_2.name, 'False', guitar_2.is_vintage()))

if __name__ == '__main__':
    main()

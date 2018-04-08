"""CP1404 Practicals - guitars list"""

from prac_07.guitar import Guitar


def main():

    my_guitars = []

    print('My Guitars!')

    """ Missing validation inputs, but works
    more_guitars = 'y'
    while more_guitars == 'y':
        name = input('Name: ')
        year = int(input('Year: '))
        cost = float(input('Cost: $'))
        temp_guitar = Guitar(name, year, cost)
        my_guitars.append(temp_guitar)
        print(temp_guitar, end=' added. \n')
        more_guitars = input('Another guitar type y or n: ')
    """

    my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    my_guitars.append(Guitar("Gibson L-6 CES", 1945, 12035.40))
    my_guitars.append(Guitar("Line alpha JTV-789", 2003, 1542.9))

    for i in range(0, len(my_guitars)):
        if my_guitars[i].is_vintage():
            vintage_string = '(vintage)'
        else:
            vintage_string = ''
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, my_guitars[i].name, my_guitars[i].year,
                                                                   my_guitars[i].cost, vintage_string))

if __name__ == '__main__':
    main()
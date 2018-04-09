"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.extension.car import Car


MENU = """Menu:
d) drive
r) refuel
q) quit"""


def main():

    print("Let's drive!")
    the_car = Car(input('Enter your car name: '))

    print(the_car)
    print(MENU)
    choice = input('Enter your choice: ')

    while choice != 'q':
        if choice == 'd':
            distance = the_car.drive(int(input('How many km do you wish to drive? ')))
            while distance < 0:
                print('Distance must be >= 0')
                distance = the_car.drive(int(input('How many km do you wish to drive? ')))
            print('The car drove {}km \n'.format(distance))
        elif choice == 'r':
            fuel = int(input('How many units of fuel do you want to add to the car? '))
            while fuel < 0:
                print('Distance must be >= 0')
                fuel = int(input('How many units of fuel do you want to add to the car? '))
            the_car.add_fuel(fuel)
            print('Added {} units of fuel.\n'.format(fuel))
        else:
            print('Invalid choice\n')

        print(the_car)
        print(MENU)
        choice = input('Enter your choice: ')

    print("Good bye {}'s driver".format(the_car.name))


if __name__ == '__main__':
    main()

"""
CP1404/CP5632 Practical (Prac_08)
Let's Drive Program (From Scratch)
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = 0
    bill_to_date = 0

    print("Let's Drive!")
    print(MENU)

    response = input().lower()
    while not response == 'q':
        if response == 'c':
            print("Taxis available:")
            for taxi in taxis:
                print(str(taxis.index(taxi)) + ' - ' + str(taxi))
            current_taxi = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(bill_to_date))
        elif response == 'd':
            requested_distance = int(input("Drive how far? "))
            taxis[current_taxi].drive(requested_distance)
            bill_to_date += taxis[current_taxi].get_fare()
            print("Your {} trip cost you {:.2f}".format(taxis[current_taxi].name,
                                                        taxis[current_taxi].get_fare()))
            taxis[current_taxi].start_fare()
            print("Bill to date: ${:.2f}".format(bill_to_date))
        else:
            print("Invalid Choice")

        print(MENU)
        response = input().lower()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    for taxi in taxis:
        print(str(taxis.index(taxi)) + ' - ' + str(taxi))


if __name__ == '__main__':
    main()
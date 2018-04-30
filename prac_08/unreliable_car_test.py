"""
CP1404/CP5632 Practical
Tests the UnreliableCar (class)
"""

from prac_08.unreliable_car import UnreliableCar

def main():
    print("Testing the UnreliableCar class")

    car_1 = UnreliableCar("Ford 1", 100, 1)
    print("\nDistance driven is {}".format(car_1.drive(40)))
    print(car_1)

    car_2 = UnreliableCar("Jeep", 100, 15)
    print("\nDistance driven is {}".format(car_2.drive(40)))
    print(car_2)

    car_3 = UnreliableCar("MarsRover", 2000, 99)
    print("\nDistance driven is {}".format(car_3.drive(400)))
    print(car_3)

    print("\nTest in a loop")
    for index in range(1,10):
        car = UnreliableCar("loopingCar", 200, 50)
        car.drive(100)
        print(car)


if __name__ == '__main__':
    main()
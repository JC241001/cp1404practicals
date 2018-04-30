"""
CP1404/CP5632 Practical
Tests the Silver Service Taxi (class)
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    print("Testing the SilverService taxi class")

    taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi_1)

    taxi_2 = SilverServiceTaxi("DoubleFancy", 120, 2)
    taxi_2.start_fare()
    taxi_2.drive(18)
    print(taxi_2)
    print("The fare for this trip is ${:.2f}".format(taxi_2.get_fare()))


if __name__ == '__main__':
    main()
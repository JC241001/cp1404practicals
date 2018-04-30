"""
CP1404/CP5632 Practical
Unreliable_Car (class) is a Car (class)
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliablity."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        if randint(0,100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven

    #
    # def __str__(self):
    #     """Return a string like a Car but with current fare distance."""
    #     return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
    #                                                          self.current_fare_distance,
    #                                                          self.price_per_km)

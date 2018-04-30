"""
CP1404/CP5632 Practical
SilverServiceTaxi (class) is a Taxi (class)
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km *= self.fanciness

    def get_fare(self):
        return  super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)
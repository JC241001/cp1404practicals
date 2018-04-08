"""CP1404 Practicals - guitar class"""

import datetime


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{} ({}) : ${:,.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

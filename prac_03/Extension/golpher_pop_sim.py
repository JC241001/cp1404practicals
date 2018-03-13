"""Simulate Gopher population over 10 year period"""


import random
import math

STARTING_POPULATION = 1000


def main():
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}\n".format(STARTING_POPULATION))
    current_population = STARTING_POPULATION

    for i in range(10):
        dead_gophers = number_dead_gophers(current_population)
        new_gophers = number_new_gophers(current_population)

        current_population += (new_gophers - dead_gophers)
        print("Year {}".format(i+1))
        print("*****")
        print("{} gophers were born, {} died.".format(new_gophers, dead_gophers))
        print("Population: {}\n".format(current_population))


def number_dead_gophers(base):
    percentage = random.uniform(5,25)/100
    return math.floor(percentage * base)


def number_new_gophers(base):
    percentage = random.uniform(10,20)/100
    return math.floor(percentage * base)


if __name__ == '__main__':
    main()
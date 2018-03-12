"""Simulate Gopher population over 10 year period"""


import random

STARTING_POPULATION =  1000

def number_of_gophers_that_die(base):
    percentage = random.uniform(5,25)
    number_of_dead_gophers = percentage * base
    return number_of_dead_gophers


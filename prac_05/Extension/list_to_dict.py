"""
CP1404/CP5632 Practical
Convert parallel list to dictionary
"""
from datetime import date

NUMBER_OF_NAMES = 2

names_to_dob = {}

for i in range(NUMBER_OF_NAMES):
    name = input('Name: ')
    dob = input('Date of Birth (dd/mm/yyyy): ')
    dob_list = dob.split('/')
    dob_tuple = tuple(dob_list)
    names_to_dob[name] = dob_tuple
    print()

for name, dob in names_to_dob.items():
    date_dob = date(int(dob[2]), int(dob[1]), int(dob[0]))
    days_old = date.today() - date_dob
    age = int(days_old.days)//365
    print('{} is {} years old'.format(name, age))

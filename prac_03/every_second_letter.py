"""Asks user for name.  Has error checking to ensure name not Blank.
Prints every second letter of provided name"""


name = input("Enter name: ")
while name == "":
    print("Must enter something")
    name = input("Enter name: ")
print("Every 2nd letter is: {}".format(name[::2]))

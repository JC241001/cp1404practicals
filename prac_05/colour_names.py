"""
CP1404/CP5632 Practical
Colour names in a dictionary
"""

COLOUR_NAMES = {'AliceBlue': '#f0f8ff', 'AntiqueWhite': '#faebd7', 'AntiqueWhite1': '#ffefdb',
                'azure1': '#f0ffff', 'azure2': '#e0eeee', 'azure3': '#c1cdcd', 'azure4': '#838b8b',
                'bisque1': '#ffe4c4', 'bisque2': '#eed5b7', 'bisque3': 'cdb79e#'}
# print(STATE_NAMES)


code = input("Enter colour: ")
while code != "":
    if code in COLOUR_NAMES:
        print(code, "is", COLOUR_NAMES[code])
    else:
        print("Invalid colour")
    code = input("Enter colour: ")

for colour, code in COLOUR_NAMES.items():
    print('{:14} is {}'.format(colour, code))

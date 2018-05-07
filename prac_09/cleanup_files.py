"""
CP1404/CP5632 Practical
File renaming and os examples
"""

# import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics')
    for dir_name, subdir_list, file_list in os.walk('.'):
        if dir_name == '.':
            continue
        os.chdir(dir_name)

        # make a new directory
        try:
            os.mkdir('temp')
        except FileExistsError:
            continue

        # loop through each file in the (original) directory
        for filename in os.listdir('.'):
            # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                os.rename(filename, 'temp/' + new_name)

        print(os.getcwd())
        os.chdir('..')

    # Repeat testing
    if os.getcwd() != 'Lyrics':
        os.chdir('..')

    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    # Clean up rest of string
    new_name = ""
    for index, char in enumerate(filename):
        prev = index - 1
        if index == 0 or filename[prev] == '_' or filename[prev] == '(':
            new_name = new_name + char.upper()
        elif (char == '(' and filename[prev] != '_') or (char.isupper() and filename[prev] != '_' and filename[
            prev] != '('):
            new_name = new_name + '_' + char
        else:
            new_name = new_name + char

    return new_name


main()

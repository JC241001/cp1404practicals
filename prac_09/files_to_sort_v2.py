"""
CP1404/CP5632 Practical
Sorting files in os version 2
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('FilesToSortV2')

    # Empty set of directory names
    dir_name_dict = {}

    # Create directories and dictionary
    file_list = os.listdir('.')
    for file in file_list:
        if os.path.isfile(file):
            file_extension = file.split('.')[1]
            if file_extension not in dir_name_dict.keys():
                dir_name = input(str('What category would you like to sort {} files into: '.format(file_extension)))
                dir_name_dict.update({file_extension: dir_name})

                try:
                    os.mkdir(dir_name)
                except FileExistsError:
                    pass

            shutil.move(file, dir_name_dict.get(file_extension) + '/' + file)

    # Print out the Directories and Contents
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

if __name__ == '__main__':
    main()

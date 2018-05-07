"""
CP1404/CP5632 Practical
Sorting files in os version 1
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('FilesToSortV1')

    # Empty set of directory names
    dir_name_set = set()

    file_list = os.listdir('.')
    for file in file_list:
        if os.path.isfile(file):
            # Populate directory set
            dir_name = file.split('.')[1]
            dir_name_set.add(dir_name)

            # skip directories that already exist
            try:
                os.mkdir(dir_name)
            except FileExistsError:
                pass

            shutil.move(file, dir_name + '/' + file)

    # Print out the Directories and Contents
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

if __name__ == '__main__':
    main()

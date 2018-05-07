"""
CP1404/CP5632 Practical
Extension - Check for missing files
"""
# import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    for dir_name, subdir_list, file_list in os.walk('.'):
        if dir_name == '.':
            continue
        os.chdir(dir_name)
        dir_name = dir_name[2:]
        for file in file_list:
            char_list = []
            with open(file) as temp_file:
                for count in range(5):
                    char_list.append(temp_file.readline(2))
                    temp_file.readline()                    # Move cursor to start of next line

            if '.i' not in char_list:
                print("{} from the {} directory is missing copyright information".format(file, dir_name))

        os.chdir('..')
        print('\n')     # Separate the directories

    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

if __name__ == '__main__':
    main()

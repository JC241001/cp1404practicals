"""
CP1404/CP5632 Practical
Extension - Check for missing files
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())


    file_list = os.listdir('.')

    for file in file_list:
        char_list = []
        with open(file) as temp_file:
            for count in range(5):
                char_list.append(temp_file.readline(2))
                temp_file.readline()                    # Move cursor to start of next line

        if '.i' not in char_list:
            print("{} is missing copyright info".format(file))


    """
    # change to desired directory
    os.chdir('FilesToSortV2')

    # Empty set of directory names
    dir_name_dict = {}

    # Create directories and dictionary
    file_list = os.listdir('.')
    for file in file_list:
        if not os.path.isfile(file):
            continue

        file_extension = file.split('.')[1]
        if not file_extension in dir_name_dict.keys():
            prompt = str('What category would you like to sort {} files into: '.format(file_extension))
            dir_name = input(prompt)
            dir_name_dict.update({file_extension:dir_name})

            try:
                os.mkdir(dir_name)
            except FileExistsError:
                pass

        shutil.move(file, dir_name_dict.get(file_extension) + '/' + file)

    """
    for dir_name, subdir_list, file_list in os.walk('.'):
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)

if __name__ == '__main__':
    main()
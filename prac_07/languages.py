"""CP1404/CP5632 Practical - Client code to use the programming language class"""
# Note that the import has a folder (module) in it.

from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    language_list = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")

    for language in language_list:
        if language.is_dynamic():
            print(language.name)

    print()
    print("The dynamically typed languages are:")
    [print(language.name) for language in language_list if language.is_dynamic()]


main()

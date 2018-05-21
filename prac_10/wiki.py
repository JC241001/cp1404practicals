"""
CP1404/CP5632 Practical
Wikipedia exercise
"""

import wikipedia
import warnings


print('Welcome to the Wikipedia interaction extravaganza')
warnings.filterwarnings("ignore")

search_phrase = input("Enter search phrase: ")
while search_phrase != '':
    try:
        handle = wikipedia.page(search_phrase)
        print('TITLE: {}'.format(handle.title))
        print('SUMMARY: {}\n'.format(wikipedia.summary(search_phrase)))
        print('URL: {}'.format(handle.url))
    except wikipedia.exceptions.DisambiguationError as e:
        handle = wikipedia.page(e.options[0])
        print('TITLE: {}'.format(handle.title))
        print('SUMMARY (suggested): {}\n'.format(wikipedia.summary(e.options[0])))
        print('URL: {}'.format(handle.url))
    except wikipedia.exceptions.PageError as f:
        print("{} does not match any pages\n".format(search_phrase))
    search_phrase = input("Enter search phrase: ")


# my_list = wikipedia.search("Graph Theory")
#
# for item in my_list:
#     print(item)
# print()
#
# print(wikipedia.suggest("Graph"))
#
# print()
#
# my_list = wikipedia.search("Graph Theory", results=3)
#
# for item in my_list:
#     print(item)
# print()
#
# print(wikipedia.summary('GitHub'))

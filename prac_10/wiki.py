"""
CP1404/CP5632 Practical
Wikipedia exercise
"""

import wikipedia


print('Welcome to the Wikipedia interaction extravaganza')

search_phrase = input("Enter search phrase: ")
while search_phrase != '':
    try:
        print('SUMMARY: {}\n'.format(wikipedia.summary(search_phrase, "html.parser", "markup_type")))
    except wikipedia.exceptions.DisambiguationError as e:
        print('SUMMARY (suggested): {}\n'.format(wikipedia.summary(e.options[0])))
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


"""
CP1404/CP5632 Practical
Wikipedia exercise
"""

import wikipedia


print('Welcome to the Wikipedia interaction extravaganza')

search_phrase = input("Enter search phrase: ")
while search_phrase != '':
    handle = wikipedia.summary(search_phrase)

    #print('Suggested title is: '.format(handle.title(search_phrase)))
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




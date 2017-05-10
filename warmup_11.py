"""Write a program to determine which is the largest file
in the current directory, as defined by:
    version 1. number of characters
    version 2. number of lines
"""

import os

filenames = os.listdir('.')
# print(files)
largest_characters = -1
largest_filename = ""
for filename in filenames:
    try:
        f = open(filename)
        number_of_characters = len(f.read())
        # number_of_characters = len(f.readlines())
        if number_of_characters > largest_characters:
            largest_filename = filename
            largest_characters = number_of_characters
        # print(number_of_characters, filename)
        f.close()
    except IsADirectoryError:
        continue
print(largest_filename, largest_characters)

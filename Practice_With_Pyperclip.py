# The GOAL is to write a script that
# a) opens a txt file -> of vocabulary from Memrise
# b) copies the name of the course and the level
# c) copies the first list of words  to CLIPBOARD
# d) pastes the data to the first column of Wordwall
# e) copies the second list of words  to CLIPBOARD
# f) pastes the data to the second column of Wordwall


# IDEA -> the fisrt list of words starts in line 5
# the length of the list is the number of lines
# from line five to length of list + 5 that would be the first list of words
# that we want to copy to clipboard

# how to copy something to clipboard in python?
import pyperclip

# get activity name
with open("test.txt", "r", encoding="utf-8") as file:
    activity_name = file.readlines()[0]

print("This is the activity name ----- > ", activity_name)


# list_length = 29
list_length = 0

with open("test.txt", "r", encoding="utf-8") as file:
    list_length += len(file.readlines())


list_length = list_length // 2 - 2
print("THIS IS THE LENGTH----->", list_length)

with open("test.txt", "r", encoding="utf-8") as file:
    first_column = file.readlines()[4 : list_length + 4]

string_first_column = "".join(first_column)

pyperclip.copy(string_first_column)

print(string_first_column)

with open("test.txt", "r", encoding="utf-8") as file:
    second_column = file.readlines()[list_length + 5 :]

string_second_column = "".join(second_column)

print(string_second_column)

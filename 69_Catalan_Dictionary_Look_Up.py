# GOAL user inserts a word ->
# the program a) goes to wordreference.com catalan dictionary
# b) scrapes the info about the word
# c) creates a file with the info

from bs4 import BeautifulSoup
import requests

# The User Inserts a word here

print("Insert Catalan Word:\n")

WORD = input()


response = requests.get(WORD)
word_definition = response.text
soup = BeautifulSoup(word_definition, "html.parser")
print(soup.prettify)

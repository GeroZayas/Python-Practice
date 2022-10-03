# GOAL user inserts a word ->
# the program a) goes to wordreference.com catalan dictionary
# b) scrapes the info about the word
# c) creates a file with the info

from bs4 import BeautifulSoup
import requests

# The User Inserts a word here

# print("Insert Catalan Word:\n")

# WORD = input()


# response = requests.get(f"https://www.wordreference.com/definicio/{WORD}")
response = requests.get(f"https://www.wordreference.com/definicio/amor")
word_definition = response.text
soup = BeautifulSoup(word_definition, "html.parser")
# print(soup.prettify)

word_definition = soup.find_all(name="div", attrs={"class": "entryLa trans clickable"})

word_definition_list = []

for text in word_definition:
    word_definition_list.append(text.ol.li.get_text)

with open("definition.txt", "w") as def_file:
    for line in word_definition_list:
        def_file.write(str(line))

print("Done")

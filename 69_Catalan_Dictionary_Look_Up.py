# GOAL user inserts a word ->
# the program a) goes to wordreference.com catalan dictionary
# b) scrapes the info about the word
# c) creates a file with the info

from bs4 import BeautifulSoup
import requests

# The User Inserts a word here

print("Insert Catalan Word:\n")

WORD = input()


response = requests.get(f"https://www.wordreference.com/definicio/{WORD}")

# response = requests.get(f"https://www.wordreference.com/definicio/amor")

word_definition = response.text
soup = BeautifulSoup(word_definition, "html.parser")
# print(soup.prettify)

# word_definition = soup.find_all(name="div", attrs={"class": "entryLa trans clickable"})


words = soup.find_all("span", class_="lemmaLa main")
word_list = []

for word in words:
    word_list.append(word.text)

# print("This is the word list->", word_list)

word_definition = soup.find_all("ol", class_="olLa")

word_definition_list = []

for text in word_definition:
    word_definition_list.append(str(text.text.split(".")).strip("[]"))

# for line in word_definition_list:
#     print(line)


with open(f"Looked Up Catalan words.txt", "a") as def_file:
    for word in word_list:
        def_file.write("***" + str(word).upper() + "***" + "\n")
    for line in word_definition_list:
        def_file.write(str(line) + "\n")
    def_file.write("-" * 70 + "\n\n")

print("Done")

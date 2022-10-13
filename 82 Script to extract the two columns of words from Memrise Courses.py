from bs4 import BeautifulSoup
import requests
import csv


WEB = input("Insert valid Memrise link: ")

response = requests.get(WEB)

words = response.text

soup = BeautifulSoup(words, "html.parser")

course_name = soup.find(name="h1", attrs={"class": "course-name"})

# TODO FIX this here> to get the level number
# how to get a strong inside a div with BeautifulSoup?

level = soup.find("strong")


catalan_words = soup.find_all(name="div", attrs={"class": "col_a col text"})
english_words = soup.find_all(name="div", attrs={"class": "col_b col text"})

catalan_words_list = []
english_words_list = []


for cat in catalan_words:
    # print(cat.get_text())
    catalan_words_list.append(cat.get_text())

for eng in english_words:
    # print(eng.get_text())
    english_words_list.append(eng.get_text())

# how to put two lists into a dictionary
words_dict = dict(zip(catalan_words_list, english_words_list))

# print(words_dict)

course_name_string = course_name.get_text().strip()
level_string = level.get_text().strip()

with open(f"{course_name_string}/{course_name_string}_{level_string}.txt", "w") as file:
    file.write("Course: " + course_name_string + "\n\n")
    file.write("Level: " + level_string + "\n\n")
    for cat in words_dict:
        file.write(f"{cat}\n")
    file.write("****" * 10 + "\n")
    for eng in words_dict.values():
        file.write(f"{eng}\n")

print("DONE")

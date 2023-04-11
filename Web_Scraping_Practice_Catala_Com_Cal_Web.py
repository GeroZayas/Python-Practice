from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://elcatalacomcal.blogspot.com/2008/03/sentir-i-escoltar.html"
)
catala_com_cal_web_page = response.text

soup = BeautifulSoup(catala_com_cal_web_page, "html.parser")

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.get("class"))

# correct_phrases = soup.find_all(name="span", style="color: #3333ff;")
# correct_phrases_text = []

# wrong_phrases = soup.find_all(name="span", style="color: #cc0000;")
# wrong_phrases_text = []

phrases = soup.find_all(name="span", attrs={"style": "color: #3333ff;"})
phrases_text = []

# print(phrases)


# print(correct_phrases)

# for phrase in correct_phrases:
#     text = phrase.getText()
#     correct_phrases_text.append(text)

# for phrase in wrong_phrases:
#     text = phrase.getText()
#     wrong_phrases_text.append(text)

for phrase in phrases:
    text = phrase.getText().replace(".", "")
    phrases_text.append(text + "\n")

# print(correct_phrases_text)

filename = "catalan_phrases.txt"

# with open(filename, mode="w", newline="") as file:
#     # for phrase in correct_phrases_text:
#     #     file.write(phrase + "\n")
#     for wrong_phrase in wrong_phrases_text:
#         file.write(wrong_phrase + "\n")

with open(filename, mode="w", newline="") as file:
    for phrase in phrases_text:
        file.write(phrase + "\n")


print("Done")

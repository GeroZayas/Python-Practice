from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("https://www.rtve.es/noticias/")
noticias_rtve = response.text

soup = BeautifulSoup(noticias_rtve, "html.parser")

maintitle = soup.find_all(name="span", attrs={"class": "maintitle"})


with open("titles.txt", "w") as file:
    for title in maintitle:
        file.write(title.get_text() + "\n\n")

print("DONE")
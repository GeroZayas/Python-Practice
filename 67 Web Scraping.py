from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("https://www.cursdecatala.com/ca/frases-fetes/")
curs_cat_frases_fetes = response.text

soup = BeautifulSoup(curs_cat_frases_fetes, "html.parser")

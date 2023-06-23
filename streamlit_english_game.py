import streamlit as st
from random import choice
import csv

# PAGE CONFIGURATION
st.set_page_config(layout="centered", page_title="English Vocabulary Game")

# Insert Image in the Page
from PIL import Image

image = Image.open("./images/english.jpeg")
st.image(image, width=400)
# WELCOME MESSAGE
st.markdown(
    """
# English *Vocabulary* Game
#### By Gero Zayas
            """
)

spanish_words = []

with open("./words.csv", "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        spanish_words.append(row["spanish"])

question = st.write(f"What is the translation of ***{choice(spanish_words)}*** in Spanish?")
# READ CSV FILE
with open("./words.csv", "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        answer = st.button(row["english"])

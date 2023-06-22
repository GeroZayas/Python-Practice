import streamlit as st
from random import choice

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

words = open("./words.txt", "r").read().split("\n")

"## How do you say?"


for word in words:
    st.button(word,help="Click to see the translation")

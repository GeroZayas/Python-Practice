import streamlit as st
from random import choice

# PAGE CONFIGURATION
st.set_page_config(layout="centered", page_title="English Vocabulary Game")

# Insert Image in the Page
from PIL import Image
image = Image.open("./images/english.jpeg")
st.image(image, width=400)
# WELCOME MESSAGE
st.markdown("""
# English *Vocabulary* Game
#### By Gero Zayas
            """)

words = [
    "Dog",
    "Rabbit",
    "Bat",
    "Horse",
    "Cat",
]

if question := st.text_input(f"How do you say **{choice(words)}** in Spanish?"):
    if question == "Paris":
        st.write("Correct!")
    else:
        st.write("Try again!")
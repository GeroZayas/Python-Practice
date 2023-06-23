import streamlit as st
from random import choice, sample
import pandas as pd


[theme]
base="dark"
primaryColor="#39ff10"
secondaryBackgroundColor="#242b71"
textColor="#fff616"
font="monospace"


# PAGE CONFIGURATION
# st.set_page_config(layout="centered", page_title="English Vocabulary Game")

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

# Load the data from the CSV file
data = pd.read_csv("./spanish_verbs.csv")
total_rows = len(data)

# Track user progress
progress = st.empty()

# Initialize variables
correct_count = 0

# Create a list of English words for the question
question_words = sample(data["English"].tolist(), 4)

# Display the question
spanish_word = choice(data["Spanish"].tolist())

st.write("### What is *'" + spanish_word + "'* in English?")

buttons = [st.button(word) for word in question_words]


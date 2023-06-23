import streamlit as st
from random import choice
import csv
import pandas as pd

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

# Load the data from the CSV file
data = pd.read_csv("./spanish_verbs.csv")
total_rows = len(data)

# Track user progress
progress = st.empty()

# Get 4 random rows from the DataFrame
random_rows = data.sample(n=4)

question_row = random_rows.sample()

# Select a random row to ask the question
question_row = random_rows.sample()

# Get the Spanish word from the selected row
spanish_word = question_row["Spanish"].values[0]

# Get the corresponding English word from the selected row
correct_english_word = question_row["English"].values[0]

# Display the question
st.write("What is '" + spanish_word + "' in English?")

message = ""
st.markdown(f"{message}")

# Create buttons for the English words
for index, row in random_rows.iterrows():
    english_word = row["English"]
    if st.button(english_word):
        # Check if the selected word is correct
        if english_word == correct_english_word:
            st.write("CORRECT")
            message = "CORRECT"
        else:
            st.write("INCORRECT")
            st.write("The correct answer is: " + correct_english_word)
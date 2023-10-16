import streamlit as st
from random import choice, sample
import pandas as pd

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

# Create a list of English words for the question
question_words = sample(data["English"].tolist(), 4)

current_word = choice(question_words)

spanish_word = data.iloc[data[data["English"] == current_word].index[0]]["Spanish"]

st.write("### What is *'" + spanish_word + "'* in English?")

# create buttons with the 4 options

button_container = st.container()

with button_container:    
    col1, col2 = st.columns(2)
    with col1:
        button1 = st.button(question_words[0])
        button2 = st.button(question_words[1])
    with col2:
        button3 = st.button(question_words[2])
        button4 = st.button(question_words[3])

# get value from the button pressed
user_answer = None

if button1:
    user_answer = question_words[0]
elif button2:
    user_answer = question_words[1]
elif button3:
    user_answer = question_words[2]
elif button4:
    user_answer = question_words[3]


if user_answer == current_word:
    button_container.write("Correct!")

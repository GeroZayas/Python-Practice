from datetime import time, datetime
import streamlit as st
from random import choice, sample
import pandas as pd
import altair as alt
import numpy as np

st.title("Streamlit Practice")

data = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}
question_container = st.container()

st.write("### Hello, *World!* :sunglasses:")

df = pd.DataFrame(
    {
        "Name": ["Geronimo", "Pocahontas", "Sitting Bull", "Crazy Horse"],
        "Job": ["Doctor", "Lawyer", "Teacher", "Engineer"],
    }
)
st.write(df)

# SLIDER
st.subheader("Slider")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

# Example 2

st.subheader("Range slider")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

# Example 3

st.subheader("Range time slider")

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader("Datetime slider")

start_time = st.slider(
    "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)

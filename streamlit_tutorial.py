import streamlit as st
from datetime import time, datetime
import numpy as np
import pandas as pd

################# BUTTON #############################

st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.write("---")

################## SELECT BOX ########################

st.header("st.selectbox")

option = st.selectbox("What is your favorite color?", ("Blue", "Red", "Green"))

st.write("Your favorite color is ", option)

st.write("---")

############# MULTI SELECT ###########################

st.header("st.multiselect")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

st.write("---")

################# CHECKBOX ###########################

st.header("st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")

st.write("---")

################# SLIDERS ###########################
st.header("st.slider")

# Example 1

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

st.write("---")
################# LINE CHART ###########################

st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

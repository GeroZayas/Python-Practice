import streamlit as st
from random import choice, sample
import pandas as pd
import altair as alt

st.title("Streamlit Practice")

data = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}
question_container = st.container()

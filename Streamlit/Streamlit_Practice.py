import streamlit as st
import pandas as pd
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


tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

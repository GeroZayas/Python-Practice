import streamlit as st

# from random import choice, sample
import pandas as pd

st.title("Rent Price in Barcelona 2014-2022")

st.header("Full 2014-2022")
df = pd.read_csv("./datasets/rent_price_barcelona_2014_2022/Barcelona_rent_price.csv")
st.write(df)

# side bar
st.sidebar.title("More Info")

st.header("Most Recent: 2022")
data_2022 = df[df["Year"] == 2022]
st.write(data_2022)

# show average rent by district
st.header("Average Rent by District")
districts = df["District"].unique()
district = st.selectbox("Select District", districts)
data_district = df[df["District"] == district]
st.write(data_district)

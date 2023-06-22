import streamlit as st

# change theme to dark
st.set_page_config(layout="wide", page_title="Streamlit Practice")
st.bar_chart({"Gero": 11, "Mar": 27, "Elisa": 17})

message = """
# My name is ***Gero***
### This is What I Like a lot:
- Programming
- Reading
- Learning Languages
"""

with open("./marp_practice_1/Alleen maar Gelukkig Snelle Lyrics/Alleen maar Gelukkig Snelle Lyrics.md", "r") as f:
    message_2 = f.read()

st.markdown(message)
st.markdown(f"""
            # Advanced Python Stuff
---
            {message_2}
            """)
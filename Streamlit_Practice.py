import streamlit as st

# change theme to dark
st.set_page_config(layout="centered", page_title="Streamlit Practice")
st.bar_chart({"Gero": 11, "Mar": 27, "Elisa": 17})

message = """
# My name is ***Gero***
### This is What I Like a lot:
- Programming 
- Reading
- Learning Languages
"""


st.markdown(message)
st.markdown(
    """
# Advanced Python Stuff

---
            """
)

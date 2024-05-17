import streamlit as st

st.title("st.session_state")


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046


st.header("Input")
col1, spacer, col2 = st.columns([3, 1, 3])
with col1:
    pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

st.session_state.name, st.session_state.age = "Gero Zayas", 32

ss = st.session_state

ss.family = [
    "Sonia",
    "Basilio",
    "Carly",
    [
        "More People",
        "Some More People",
        ["uno", "dos", "tres"],
    ],
]

printeame_esto = st.write

st.header("Output")
st.write("st.session_state object:", st.session_state)

printeame_esto("My life is great!")

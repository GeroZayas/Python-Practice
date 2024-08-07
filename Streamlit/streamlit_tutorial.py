import streamlit as st
from datetime import time, datetime
import numpy as np
import pandas as pd
import time as tm

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

################# LINE CHART ############################

st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Gero", "Elisa", "Sonia"])

st.line_chart(chart_data)

st.write("---")

################# LATEX ############################

st.header("st.latex")

st.latex(
    r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)

st.write("---")

################# SECRETS ############################
st.header("Secrets")
st.write(st.secrets["message"])


st.write("---")

################# PROGRESS ############################
st.header("st.progress")

with st.expander("About this app"):
    st.write(
        "You can now display the progress of your calculations in a Streamlit app with the `st.progress` command."  # noqa: E501
    )

my_bar = st.progress(0)

for percent_complete in range(100):
    tm.sleep(0.05)
    my_bar.progress(percent_complete + 1)

# st.balloons()


st.write("---")

################# FORM ############################

st.header("st.form")

# Full example of using the with notation
st.header("1. Example of using `with` notation")
st.subheader("Coffee machine")

with st.form("my_form"):
    st.subheader("**Order your coffee bitch**")

    # Input widgets
    coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
    coffee_roast_val = st.selectbox("Coffee roast", ["Light", "Medium", "Dark"])
    brewing_val = st.selectbox(
        "Brewing method", ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"]
    )
    serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    owncup_val = st.checkbox("Bring own cup")

    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    st.markdown(
        f"""
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        """
    )
else:
    st.write("☝️ Place your order!")


# Short example of using an object notation
st.header("2. Example of object notation")

form = st.form("my_form_2")
selected_val = form.slider("Select a value")
form.form_submit_button("Submit")

st.write("Selected value: ", selected_val)


st.write("---")

################# INFO and EXPANDER ############################

st.header("st.info")
st.info("This is a purely informational message", icon="📡")

st.header("st.expander")
with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)


st.write("---")

################# INFO and EXPANDER ############################

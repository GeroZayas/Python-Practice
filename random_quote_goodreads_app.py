import requests
import streamlit as st
from bs4 import BeautifulSoup

# Function to fetch the quote from the website
def get_quote():
    url = "https://www.goodreads.com/work/quotes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote_div = soup.find('div', class_='leftContainer mediumText')
    return quote_div.find('p').text.strip()



# Main Streamlit app
def main():
    st.markdown("<h1 style='text-align: center; color: darkred;'>Quote of the Day</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #555;'>Click below to get a new quote:</h2>", unsafe_allow_html=True)
    
    # Button to fetch and display the quote
    if st.button("Get Quote"):
        quote = get_quote()
        st.markdown(f"<h2 style='text-align: center; color: #111;'>{quote}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

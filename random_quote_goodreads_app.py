import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_quotes(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quoteText')
    return [quote.get_text(strip=True) for quote in quotes]

def main():
    st.title("Goodreads Author Quotes Scraper")
    st.write("Enter the Goodreads author quotes page URL:")

    page_url = st.text_input("Page URL", "")
    if st.button("Scrape Quotes"):
        if page_url:
            quotes = scrape_quotes(page_url)
            st.write("Scraped Quotes:")
            for quote in quotes:
                st.write(quote)
        else:
            st.write("Please enter a valid page URL.")

if __name__ == "__main__":
    main()

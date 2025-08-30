import httpx
from bs4 import BeautifulSoup
from rich import print
from random import choice


def scraper(url: str) -> str:
    """
    Scrapes the content of a given url. In a very NICEEEE way
    
    @param url: str
    @rval clean scraped content: str
    
    """
    response = httpx.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    
    clean = soup.get_text(strip=True)

    # return soup.get_text(strip=True)
    return clean

def random_name():
    """
    Returns a random name from a list of names
    """
    names = "gero mar sonia basilio migdalia zayas elisa kike".split()
    
    return choice(names)


if __name__ == "__main__":
    user_provided_url = input("insert url: ")
    
    if user_provided_url.strip() == "":
        url = "https://es.wikipedia.org/wiki/Gero"

    url = user_provided_url

    try:
        r = scraper(url)
        print(r)
    except Exception as e:
        print("There has been an error:", e)

    
import requests
from bs4 import BeautifulSoup

base_url = "https://paulvanderlaken.com/category/automation/page/2/"

# Start from page 1 and keep track of the current page
page_number = 0
has_next_page = True

while has_next_page:
    if base_url == "https://paulvanderlaken.com/category/automation/":
        has_next_page = False
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the links to blog posts
    links = soup.find_all("header", class_="entry-header")

    # Extract and print the URLs
    for link in links:
        print(link.a.text, link.a, "\n\n")

    page_number += 1

if __name__ == "__main__":
    pass

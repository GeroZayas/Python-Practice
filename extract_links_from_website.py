import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage content
url = "http://www.futuridiomes.com"  # Replace with your target URL
response = requests.get(url)

# Step 2: Parse the HTML and find links
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")

# Step 3: Extract and print the links
for link in links:
    href = link.get("href")
    if href:
        print(href)

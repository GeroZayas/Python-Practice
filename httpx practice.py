import httpx
from bs4 import BeautifulSoup


artist = input("Artist: ")
song = input("Song: ")

params = {
    "artist": artist,
    "song": artist,
}

response = httpx.get(f"https://www.azlyrics.com/lyrics/{artist}/{song}.html")

soup = BeautifulSoup(response.content, "html.parser")

# Extract the title of the page
title = soup.title.string
print(title)

print("Response's status code:\n->", response.status_code)

print("Response's headers:\n->", response.headers)

print("Response's text:\n->", response.text)

import httpx
from bs4 import BeautifulSoup

artist = None
song = None


# Asking the user to input the artist and song name.
if not artist and not song:
    artist = input("Artist: ").lower().strip().replace(" ", "")
    song = input("Song: ").lower()

# print("Artist", artist)
# print("Song", song)

params = {
    "artist": artist,
    "song": artist,
}

# Making a request to the website and getting the response.
response = httpx.get(f"https://www.azlyrics.com/lyrics/{artist}/{song}.html")

soup = BeautifulSoup(response.content, "html.parser")


# Extract the title of the page
title = soup.title.string
print(title)

print("-" * 60)
content = soup.select_one(".col-xs-12 > div:nth-child(8)").text.strip()
print(content)
print("-" * 60)

import httpx
from bs4 import BeautifulSoup

artist = None
song = None

# FUNCTIONS
# ----------------------------------------------------------------

# ----------------------------------------------------------------

# Asking the user to input the artist and song name.
if not artist and not song:
    artist = input("Artist: ")
    artist_str_fixed = artist.lower().strip().replace(" ", "")
    song = input("Song: ")
    song_str_fixed = song.lower().strip().replace(" ", "")


# Making a request to the website and getting the response.
response = httpx.get(
    f"https://www.azlyrics.com/lyrics/{artist_str_fixed}/{song_str_fixed}.html"
)

soup = BeautifulSoup(response.content, "html.parser")

# Extract the title of the page
title = soup.title.string
print(title)

print("-" * 60)
content = soup.select_one(".col-xs-12 > div:nth-child(8)").text.strip()
print(content)
print("-" * 60)

with open(
    f"./azlyrics_downloads/{artist.capitalize()}_{song.capitalize()}.txt",
    "w",
    encoding="utf-8",
) as file:
    for line in content.splitlines():
        file.write(line + "\n")

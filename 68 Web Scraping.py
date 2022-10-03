from bs4 import BeautifulSoup
import requests
import csv

# https://www.viasona.cat/grup/4hiverns/4hiverns/miralls

WEB = "https://www.viasona.cat/grup/4hiverns/4hiverns/miralls"


# GOAL Get lyrics from this page

response = requests.get(WEB)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify)

song_title = soup.find(name="h1", attrs={"class": "titol-pagina"})

# print("Song: ", song_title.text)

group_or_singer = soup.find(name="h2", attrs={"class": "subtitol-pagina"})

# print("Group:", group_or_singer.text)

lyrics = soup.find_all(
    name="div", attrs={"class": "enc-lletra__lletra user-text seleccionable"}
)


song_lyrics = []
song_lyrics.append(song_title.text)
song_lyrics.append(group_or_singer.text)

# print(song_lyrics)

for lyric in lyrics:
    song_lyrics.append(lyric.text)

with open(f"{song_title.text} from {group_or_singer.text}.txt", "w") as lyrics_file:
    for line in song_lyrics:
        lyrics_file.write(line)

print("Done")

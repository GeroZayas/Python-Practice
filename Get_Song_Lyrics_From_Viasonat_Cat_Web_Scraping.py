from bs4 import BeautifulSoup
import requests
import csv

# TODO -> create a GUI to run this program
# TODO -> use TYPER for CLI implementation


def get_lyric_save_on_txt_file(link=None):
    # The User Inserts here a valid viasona.cat link of a song lyric

    if link == None:
        print("Insert Web Link from Viasona.Cat:\n")
        WEB = input()

    else:
        WEB = link

    response = requests.get(WEB)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")
    # print(soup.prettify)

    # We get hold of the title here
    song_title = soup.find(name="h1", attrs={"class": "titol-pagina"})

    # print("Song: ", song_title.text)

    # We get hold of the group name or singer here
    group_or_singer = soup.find(name="h2", attrs={"class": "subtitol-pagina"})

    # print("Group:", group_or_singer.text)

    # We get hold of the lyrics here
    lyrics = soup.find_all(
        name="div", attrs={"class": "enc-lletra__lletra user-text seleccionable"}
    )

    # Declare a new list and append name of song and group
    song_lyrics = []
    song_lyrics.append("Title: " + song_title.text + "\n\n")
    song_lyrics.append("Group / Singer: " + group_or_singer.text + "\n\n")

    # print(song_lyrics)

    # We now append all the lyrics, line by line
    for lyric in lyrics:
        song_lyrics.append(lyric.text)

    # We create a new .txt file and add the lyrics to it
    with open(
        f"lyrics_from_viasona/{song_title.text} from {group_or_singer.text}.txt", "w"
    ) as lyrics_file:
        for line in song_lyrics:
            lyrics_file.write(line)

    print("Done")


if __name__ == "__main__":
    get_lyric_save_on_txt_file()
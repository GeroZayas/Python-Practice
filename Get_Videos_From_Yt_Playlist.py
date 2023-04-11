# PURPOSE Get video names, links and duration from a given youtube playlist
# ----------------------------------------------------------------
from pytube import Playlist, YouTube
import json
from itertools import groupby
from tqdm import tqdm
from markdown import markdown
import time
import re

playlist_link = input("Insert playlist: \n>>> ")

# Playlist Python Gero Zayas:
# playlist_link = (
#     "https://www.youtube.com/playlist?list=PLKLTYrrEuv2OahdLdELlP0X5XXYmWFb-B"
# )


# # Playlist to tinker
# playlist_link = (
#     "https://www.youtube.com/playlist?list=PLOkVupluCIjtA034kJfn1ulwBoGjmKJ_2"
# )


list_of_video_urls = Playlist(playlist_link)

lenght_of_playlist = list_of_video_urls.length


playlist_name = list_of_video_urls.title

print(f"Playlist Title: {playlist_name}")


def write_markdown(file, title, author, url):
    file.write(markdown("-" * 3))  # space
    file.write(markdown(f"**Title**: *{title}*"))
    file.write(markdown(f"**Author**: {author}"))
    file.write(markdown(f"**Url**: [link]({url})"))
    print(title)


errors = []


def extraction():
    counter: int = 1

    with open(f"{playlist_name}.md", "w", encoding="utf-8") as html_file:
        for i, video in enumerate(list_of_video_urls):
            index, video_url = i, video
            try:
                write_markdown(
                    file=html_file,
                    author=YouTube(video).author,
                    title=YouTube(video).title,
                    url=list_of_video_urls[i],
                )
                print(counter, f"/{lenght_of_playlist}")
                counter += 1
            except Exception as e:
                print("-" * 60)
                print(f"This ocurred: {e}\n")
                url = re.search("(?P<url>https?://[^\s]+)", str(e)).group("url")[:-1]
                errors.append(url)

            finally:
                continue


extraction()


if len(errors) > 0:
    for e in errors:
        print(e)

    with open(f"{playlist_name}_errors.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write("These videos couldn't be fetched:")
        for i, video in enumerate(errors):
            index, video_url = i, video
            txt_file.write(video)

    with open(f"{playlist_name}_errors.md", "w", encoding="utf-8") as html_file:
        for i, video in enumerate(errors):
            index, video_url = i, video
            try:
                write_markdown(
                    file=html_file,
                    title=YouTube(video).title,
                    author=YouTube(video).title,
                    url=video,
                )
            except Exception as e:
                print(e)

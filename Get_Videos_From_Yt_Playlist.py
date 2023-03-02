# PURPOSE Get video names, links and duration from a given youtube playlist
# ----------------------------------------------------------------
from pytube import Playlist, YouTube
import json
from itertools import groupby
from tqdm import tqdm

# playlist_link = input("Insert playlist lisk: \n>>>")

# # Playlist Python Gero Zayas:
# playlist_link = (
#     "https://www.youtube.com/playlist?list=PLKLTYrrEuv2OahdLdELlP0X5XXYmWFb-B"
# )


# Playlist Python pywin32 series
playlist_link = (
    "https://www.youtube.com/playlist?list=PL3JVwFmb_BnT0MYLMQsNKql_gec_W2tja"
)


list_of_video_urls = Playlist(playlist_link)


for i, video in enumerate(list_of_video_urls):
    try:
        print("-" * 60)  # space
        print("The title: ", YouTube(video).title)
        print("The author: ", YouTube(video).author)
        print("The video url: ", list_of_video_urls[i])
    except Exception as e:
        print(f"This ocurred: {e}\n")
        continue


# list_of_authors = []

# # for url in tqdm(list_of_video_urls):
# #     list_of_authors.append(YouTube(url).author)

# print(list_of_authors)


# def group_videos_by_author(x):
#     return x[0]


# group_data = groupby(list_of_video_urls)

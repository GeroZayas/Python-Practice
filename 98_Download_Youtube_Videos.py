# Youtube Downloade.remove()

from pytube import YouTube
import os
from pathlib import Path

link = input("Enter link here: ")

url = YouTube(link)

print("downloading....")

video = url.streams.get_highest_resolution()


path_to_download_folder = r"C:\Users\Gero Zayas\Downloads"

video.download(path_to_download_folder)

print(f"Downloaded! :) here => {path_to_download_folder}")


# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

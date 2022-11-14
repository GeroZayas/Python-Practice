# Youtube Downloader

import os
from pathlib import Path

from pytube import YouTube


from playsound import playsound as play

# link = input("Enter link here: ")

list_of_links = []

running = True

while running:
    print("Insert link")
    new_link = input("HERE: ")
    list_of_links.append(new_link)

    user_answer = input(
        """
          Another link? 
          
          Press 'y' or 'n'
          
          """
    )

    print()  # add a line break

    if user_answer == "n" or user_answer == "N":
        break
    elif user_answer == "y" or user_answer == "Y":
        continue
    else:
        print("WRONG INPUT")
        break


# for link in list_of_links:
#     print(link[0:5])

counter = 0
for link in list_of_links:

    print("--" * 30)

    counter += 1
    if link[0:5] == "https":

        url = YouTube(link)

        video_size_bytes = url.streams.get_highest_resolution().filesize
        # video_size_bytes = url.streams.get_by_itag(17).filesize
        video_size_mb = f"{video_size_bytes/1048576:.2f} MB"
        print("This is the video's size", video_size_mb)

        video_name = url.streams[0].title
        print(f"downloading.... {counter} => {video_name}")

        video = url.streams.get_highest_resolution()

        path_to_download_folder = (
            r"C:\Users\Gero Zayas\Downloads\Downloaded_from_YouTube"
        )

        video.download(path_to_download_folder)

        print()  # add a line break
        print(f"Downloaded! :) here => {path_to_download_folder}")
        play("./sounds/video_dowloaded.mp3")

    else:
        print("video url incorrect")

print(
    """

      ALL DONE BABY!!!

      """
)
play("./sounds/all_dowloads_completed.mp3")


# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

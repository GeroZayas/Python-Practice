# Youtube Downloader

# TODO: create a txt file with names of videos downloaded and time and date of download
# TODO: create a progress bar to show the videos being downloaded

import os
from pathlib import Path

from pytube import YouTube

# we import playsound to be use sound markers after some tasks are completed or run
from playsound import playsound as play


# We create a list of links to save them and be able to iterate over them later
list_of_links = []

# we create a boolean value 'running' to set program to be running or not
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
        print("WRONG INPUT\n")
        continue


# We create a counter to number the elements being downloaded
counter = 0
for link in list_of_links:

    print("--" * 30)

    counter += 1

    # We check if the input link is valid, only true if it starts with 'https'
    if link[0:5] == "https":

        url = YouTube(link)

        # Here we want to know how big the file is and we let the user know
        video_size_bytes = url.streams.get_highest_resolution().filesize

        # video_size_bytes = url.streams.get_by_itag(17).filesize

        # we convert bytes to megabytes to make more readable
        video_size_mb = f"{video_size_bytes/1048576:.2f} MB"
        print("This is the video's size", video_size_mb, "\n")

        video_name = url.streams[0].title
        print(f"downloading.... {counter} => {video_name}\n")

        video = url.streams.get_highest_resolution()

        path_to_download_folder = (
            r"C:\Users\Gero Zayas\Downloads\Downloaded_from_YouTube"
        )

        try:
            video.download(path_to_download_folder)
            print()  # add a line break
            print(f"Downloaded! :) here => {path_to_download_folder}")
            play("./sounds/video_dowloaded.mp3")
        except Exception:
            print(
                f"\nVideo -> {video_name} not downloaded -> SOME PROBLEM TOOK PLACE\n"
            )
            # play("./sounds/some_video_didnt_work (enhanced).wav")
            continue

    else:
        print("video url incorrect")

# --------------------- SAVE TXT FILE WITH DATA FROM PROGRAM ------------


# --------------------- PROGRAM COMPLETED -------------------------------
print(
    """

      ALL DONE BABY!!!

      """
)
play("./sounds/all_dowloads_completed.mp3")

# -----------------------------------------------------------------------

# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

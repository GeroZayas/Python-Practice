# Youtube Downloader

# TODO: create a txt file with names of videos downloaded and time and date of download
# TODO: create a progress bar to show the videos being downloaded

import os

# from pathlib import Path

# -------------- IMPORT PRETTY TABLE -------------------------------
from prettytable import PrettyTable

# -----------------------------------------------------------------------

# We import datetime to print the date of downloaded videos later
import datetime

date_time = datetime.datetime.now()

the_date = date_time.strftime("%B %d %Y - %I %M %p")

# -----------------------------------------------------------------------

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

# ---------------------------------------------------------------------

# ------------------------ CREATE PRETTY TABLE ------------------------

table_of_videos = PrettyTable(["Name of Video", "Size", "Date"])
table_of_videos.padding_width = (
    1  # One space between column edges and contents (default)
)

# Aligning columns
table_of_videos.align["Name of Video"] = "l"
table_of_videos.align["Size"] = "c"
table_of_videos.align["Date"] = "c"
table_of_videos._max_width = {"Name of Video": 30}

# ---------------------------------------------------------------------

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

            # add row to pretty table
            table_of_videos.add_row(
                [
                    f"{video_name}",
                    f"{video_size_mb}",
                    f"{the_date}",
                ]
            )

            # we play the sound of successful download
            try:
                play("./sounds/video_dowloaded.mp3")
            except Exception:
                pass

        except Exception:
            print(
                f"\nVideo -> {video_name} not downloaded -> SOME PROBLEM TOOK PLACE\n"
            )
            # play("./sounds/some_video_didnt_work (enhanced).wav")
            continue

    else:
        print("video url incorrect")

# --------------------- SAVE TXT FILE WITH DATA FROM PROGRAM -----------


try:
    with open(
        f"{path_to_download_folder}\Downloaded Videos on {the_date}.doc", "w"
    ) as w:
        w.write(str(table_of_videos))
except Exception:
    pass

# --------------------- PROGRAM COMPLETED ------------------------------
print(
    """

      ALL DONE BABY!!!

      """
)

try:
    play("./sounds/all_dowloads_completed.mp3")
except Exception:
    pass
# ----------------------------------------------------------------------

# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

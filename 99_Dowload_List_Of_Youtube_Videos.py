# Youtube Downloader

# TODO: create a progress bar to show the videos being downloaded

import os
from rich import print

# from rich.progress import track


# from pathlib import Path

# -----------------------------------------------------------------------

# We import datetime to print the date of downloaded videos later
import datetime

date_time = datetime.datetime.now()

the_date = date_time.strftime("%B %d %Y - %I %M %p")

# -----------------------------------------------------------------------

from pytube import YouTube

# we import playsound to be use sound markers after some tasks are completed or run
from playsound import playsound as play


# -----------------------------------------------------------------------

# ---------- PRINT TITLE ---------------

# print(f"[bold yellow]{title}[/bold yellow]")

print(
    """
                        [bold yellow]+-+-+-+-+-+-+        
                        | G e r o ' s |        
                            +-+-+[/bold yellow][bold red]-+-+-+-+-+     
                            | Y o u t u b e |      
                            +-+-+-+-+-+-+-+[/bold red][bold blue]-+-+-+
                                    [bold blue]| D o w n l o a d e r |
                                    +-+-+-+-+-+-+-+-+-+-+[/bold blue]
      """
)

# ---------- END OF PRINT TITLE ---------------
# -----------------------------------------------------------------------



# We create a list of links to save them and be able to iterate over them later
list_of_links = []

# we create a boolean value 'running' to set program to be running or not
running = True

while running:
    print("[bold yellow]Insert Link[/bold yellow]")
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

# We create a counter to number the elements being downloaded
counter = 0
for link in list_of_links:

    print("[bold yellow]--[/bold yellow]" * 30)

    counter += 1

    # We check if the input link is valid, only true if it starts with 'https'
    if link[0:5] == "https":

        url = YouTube(link)

        # Here we want to know how big the file is and we let the user know
        video_size_bytes = url.streams.get_highest_resolution().filesize

        # video_size_bytes = url.streams.get_by_itag(17).filesize

        # we convert bytes to megabytes to make more readable
        video_size_mb = f"{video_size_bytes/1048576:.2f} MB"
        print("[bold blue]This is the video's size[/bold blue]", video_size_mb, "\n")

        video_name = url.streams[0].title
        print(f"[bold yellow]downloading....[/bold yellow] {counter} => {video_name}\n")

        video = url.streams.get_highest_resolution()

        path_to_download_folder = (
            r"C:\Users\Gero Zayas\Downloads\Downloaded_from_YouTube"
        )

        try:
            video.download(path_to_download_folder)
            print()  # add a line break
            print(
                f"[bold red]Downloaded! :) here => [/bold red] {path_to_download_folder}"
            )

            # --------------------- SAVE TXT FILE WITH DATA FROM PROGRAM -----------

            try:
                with open(
                    f"{path_to_download_folder}\Downloaded Videos.txt", "a"
                ) as file:
                    file.write(
                        f"""
{video_name} -> {the_date}
                               """
                    )
            except Exception:
                pass

            # we play the sound of successful download
            try:
                play("./sounds/video_dowloaded.mp3")
            except Exception:
                pass

        except Exception:
            print(
                f"\n[bold yellow]Video ->[/bold yellow] {video_name} not downloaded -> SOME PROBLEM TOOK PLACE\n"
            )
            # play("./sounds/some_video_didnt_work (enhanced).wav")
            continue

    else:
        print("video url incorrect")


# --------------------- PROGRAM COMPLETED ------------------------------

print(
    """

      [bold green]ALL DONE BABY!!![/bold green]

      """
)


try:
    play("./sounds/all_dowloads_completed.mp3")
except Exception:
    pass


# ----------------------------------------------------------------------

# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

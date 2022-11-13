# Youtube Downloade.remove()

from pytube import YouTube
import os
from pathlib import Path

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

    print() # add a line break

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

        print(f"downloading.... {counter} => {link}")

        video = url.streams.get_highest_resolution()

        path_to_download_folder = r"C:\Users\Gero Zayas\Downloads"

        video.download(path_to_download_folder)

        print()  # add a line break
        print(f"Downloaded! :) here => {path_to_download_folder}")
    else:
        print("video url incorrect")

print(
    """

      ALL DONE BABY!!!

      """
)


# this would save the file on the same folder as the script
# print(f"Downloaded! :) here => {os.path.abspath(os.getcwd())}")

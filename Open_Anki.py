# Automation Practice

# go here for more https://automatetheboringstuff.com/2e/chapter17/

import subprocess

print("This script will open Anki.exe automatically")
print("Is that what you want?")
user_answer = input("y or n: ")

if user_answer == "y":
    subprocess.Popen("C:\Program Files\Anki\Anki.exe")
    print("Anki.exe opened")

# subprocess.Popen("C:\Program Files\Anki\Anki.exe")

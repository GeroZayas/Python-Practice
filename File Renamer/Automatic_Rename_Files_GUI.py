# This program automatically changes the name of the each file in the current folder
# It gets hold of the first 14 words in each file to rename it
# It works with *.docx , *.md, *.txt files

import PySimpleGUI as sg
import os
import docx
import re

sg.theme("DarkTeal9")

# Define the layout of the GUI
layout = [
    [sg.Text("Select a folder to rename files:")],
    [sg.Text("Folder:", size=(8, 1)), sg.InputText(), sg.FolderBrowse()],
    [sg.Button("Rename Files")],
]

# Create the window
window = sg.Window("File Renamer", layout)

# Event Loop
while True:
    event, values = window.Read()
    if event in (None, "Cancel"):  # if user closes window or clicks cancel
        break
    if event == "Rename Files":
        # Get the selected folder
        directory = values[0]
        if directory in ["", " ", "  ", "   "]:
            sg.Popup("Insert correct folder path")
        # Loop through all files in the selected folder
        else:
            for filename in os.listdir(directory):
                if (
                    filename.endswith(".txt")
                    or filename.endswith(".docx")
                    or filename.endswith(".md")
                ):
                    # Open the file
                    if filename.endswith(".txt"):
                        with open(
                            os.path.join(directory, filename), "r", encoding="utf-8"
                        ) as f:
                            first_line = f.readline()
                    elif filename.endswith(".docx"):
                        doc = docx.Document(os.path.join(directory, filename))
                        first_line = doc.paragraphs[0].text
                    elif filename.endswith(".md"):
                        with open(
                            os.path.join(directory, filename), "r", encoding="utf-8"
                        ) as f:
                            try:
                                first_line = f.readline()
                            except UnicodeDecodeError:
                                continue
                    # Extract the first 7 words
                    first_14_words = first_line.split()[:14]
                    # Remove symbols and keep only letters and numbers
                    new_filename = (
                        "_".join(re.findall(r"\b\w+\b", " ".join(first_14_words)))
                        + filename[-4:]
                    )
                    # Rename the file
                    os.rename(
                        os.path.join(directory, filename),
                        os.path.join(directory, new_filename),
                    )
            sg.Popup("Files have been successfully renamed.")

window.Close()

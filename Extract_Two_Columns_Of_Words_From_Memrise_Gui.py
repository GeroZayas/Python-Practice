import PySimpleGUI as sg
from Extract_Vocab_From_Memrise_Courses import extract_vocab

# TODO: a) add progress bar to visualize process
# TODO: b) ask if user wants to download another link (while loop?)
# TODO: c) Beautify the GUI
# TODO: d) Add own icon
# TODO: e)

import os

os.system("cls")

FONT = "Consolas 14"

sg.theme("Sandy Beach")


# Define the window's contents
layout = [
    [sg.Input(key="-INPUT-", size=80, font=FONT)],
    [
        sg.Text(
            text="INSERT LINK and WAIT TILL WE GET ALL THE VOCABULARY!",
            size=(80, 1),
            key="-OUTPUT-",
            font=FONT,
        )
    ],
    [sg.ProgressBar(max_value=1000, orientation="h", size=(73, 15), key="-PROG-")],
    [sg.Button("Ok", font=FONT, bind_return_key=True), sg.Button("Quit", font=FONT)],
]

# Create the window
window = sg.Window("Get Vocabulary from Memrise Course", layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

        # Output a message to the window
    window["-OUTPUT-"].update("INSERT LINK and WAIT TILL WE GET ALL THE VOCABULARY!")

    # GET THE LINK
    extract_vocab(link=values["-INPUT-"])

    the_percentage = extract_vocab.percentage

    window["-OUTPUT-"].update("OK! DONE!")

    # print(the_percentage)

# Finish up by removing from the screen
window.close()
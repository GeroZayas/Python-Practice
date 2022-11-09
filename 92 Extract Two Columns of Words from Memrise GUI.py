import PySimpleGUI as sg
from Extract_Vocab_From_Memrise_Courses import extract_vocab

# TODO: a) add progress bar to visualize process
# TODO: b) ask if user wants to download another link (while loop?)
# TODO: c) Beautify the GUI
# TODO: d) Add own icon
# TODO: e)


# Define the window's contents
layout = [
    [sg.Input(key="-INPUT-", size=80)],
    [
        sg.Text(
            text="INSERT LINK and WAIT TILL WE GET ALL THE VOCABULARY!",
            size=(80, 1),
            key="-OUTPUT-",
        )
    ],
    [sg.Button("Ok"), sg.Button("Quit")],
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

    window["-OUTPUT-"].update("OK! DONE!")


# Finish up by removing from the screen
window.close()

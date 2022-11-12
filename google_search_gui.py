# GOAL: Make a GUI program to look up something on Google from desktop
import PySimpleGUI as sg
import webbrowser


sg.theme("DarkBlue7")

# Define the window's contents
layout = [
    [sg.Text("Look it up on Google:")],
    [
        sg.Input(
            key="-INPUT-",
            text_color="yellow",
            font="Consolas 16",
            do_not_clear=False,
        )
    ],
    [
        sg.Button(
            "LOOK IT UP!",
            mouseover_colors="red",
            bind_return_key=True,
        ),
        sg.Button("Quit"),
    ],
]

# Create the window
window = sg.Window("Window Title", layout, icon="./google.ico")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    else:
        look_up = values["-INPUT-"]

        url = f"https://google.com/search?q={look_up}"
        webbrowser.get(
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        ).open(url)

# Finish up by removing from the screen
window.close()

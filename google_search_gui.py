# GOAL: Make a GUI program to look up something on Google from desktop
import PySimpleGUI as sg
import webbrowser


sg.theme("DarkAmber")

# Define the window's contents
layout = [
    [sg.Text("Look it up on Google:")],
    [
        sg.Input(
            key="-INPUT_GOOGLE-",
            # text_color="yellow",
            font="Consolas 15",
            do_not_clear=False,
        )
    ],
    [sg.Text("Look it up on Youtube:")],
    [
        sg.Input(
            key="-INPUT_YOUTUBE-",
            # text_color="red",
            font="Consolas 15",
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
window = sg.Window("Google & YouTube Look-up-er", layout, icon="./google.ico")

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    else:
        if values["-INPUT_GOOGLE-"]:
            look_up = values["-INPUT_GOOGLE-"]

            url = f"https://google.com/search?q={look_up}"
        elif values["-INPUT_YOUTUBE-"]:
            look_up = values["-INPUT_YOUTUBE-"]
            url = f"https://www.youtube.com/results?search_query={look_up}"
        webbrowser.get(
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        ).open(url)

# Finish up by removing from the screen
window.close()

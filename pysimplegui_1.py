import PySimpleGUI as sg

layout = [
    [sg.Text("Learn English Now!", background_color="darkred", font=("Arial", 30))],
    [
        sg.Button(
            button_text="Go to second window!",
            mouseover_colors="green",
            button_color="darkgreen",
            font=("Arial", 14),
        )
    ],
    [
        sg.Button(
            button_text="Exit!",
            mouseover_colors="green",
            button_color="darkgreen",
            font=("Arial", 14),
        )
    ],
]

layout_2 = [
    [sg.Text("Second Window!", background_color="darkred", font=("Arial", 30))],
    [
        sg.Button(
            button_text="Go to first window!",
            mouseover_colors="green",
            button_color="darkgreen",
            font=("Arial", 14),
        )
    ],
    [
        sg.Button(
            button_text="Exit!",
            mouseover_colors="green",
            button_color="darkgreen",
            font=("Arial", 14),
        )
    ],
]

window = sg.Window(
    "Learn English Now!", layout=layout, size=(400, 200), background_color="gold"
)

# create a second window
window2 = sg.Window(title="Second Window", layout=layout_2, size=(400, 200))

while True:
    event, values = window.read()  # type: ignore
    if event == "Go to second window!":
        # hide the first window
        window.hide()
        # show the second window
        window2.read()  # type: ignore
    if event in [sg.WINDOW_CLOSED, "Exit!"]:
        break

window.close()

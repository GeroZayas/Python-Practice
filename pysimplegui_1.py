import PySimpleGUI as sg

layout = [
    [sg.Text("Learn English Now!", background_color="darkred", font=("Arial", 30))],
    [sg.Button(button_text="GO!", mouseover_colors="blue", button_color="darkgreen", font=("Arial", 14))],
]

window = sg.Window(
    "Learn English Now!", layout=layout, size=(400, 200), background_color="gold"
)

while True:
    event, values = window.read()  # type: ignore
    if event in [sg.WINDOW_CLOSED, "GO!"]:
        break

window.close()

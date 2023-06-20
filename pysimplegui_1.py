import PySimpleGUI as sg

layout = [
    [sg.Text("Learn English Now!")],
    [sg.Button('GO!')]
]

window = sg.Window("Learn English Now!", layout=layout)

while True:
    event, values = window.read() # type: ignore
    if event in [sg.WINDOW_CLOSED, "GO!"]:
        break

window.close()
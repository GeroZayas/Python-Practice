import PySimpleGUI as sg

layout1 = [
    [sg.Text('Window 1')],
    [sg.Button('Go to Window 2')]
]

layout2 = [
    [sg.Text('Window 2')],
    [sg.Button('Go back to Window 1')]
]

window1 = sg.Window('Window 1', layout1)
window2 = None

while True:
    event1, values1 = window1.read()

    if event1 == sg.WINDOW_CLOSED:
        break

    if event1 == 'Go to Window 2':
        window1.Hide()
        window2 = sg.Window('Window 2', layout2)

    if window2 is not None:
        event2, values2 = window2.read() # type: ignore

        if event2 == sg.WINDOW_CLOSED:
            window2.close()
            window2 = None
            window1.un_hide()

window1.close()

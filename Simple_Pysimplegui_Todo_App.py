import PySimpleGUI as sg

# Set the theme for the pysimplegui window
sg.theme("Default")

# Create the layout for the main todo app window
layout = [
    [sg.Text("Todo App", font=("Consolas", 12))],
    [sg.Input(key="task")],
    [sg.Button("Add Task")],
    [sg.Listbox(values=[], key="tasks", font=("Consolas", 12))],
    [sg.Button("Remove Task")],
    [sg.Button("Close")],
]

# Create the window object
window = sg.Window("Todo App", layout)

# Create an empty list to store the tasks
tasks = []

# The main event loop
while True:
    # Get the event and values from the window
    event, values = window.read()

    # If the user closes the window, break out of the loop
    if event == sg.WIN_CLOSED:
        break

    # If the user clicks the 'Add Task' button, ask them for the reason
    # the task is important, then add the task and reason to the list
    # of tasks
    if event == "Add Task":
        reason = sg.popup_get_text("Why is this task important?")
        tasks.append({"*": values["task"], "->": reason})
        window["tasks"].update(values=tasks)

    # If the user clicks the 'Remove Task' button, remove the selected
    # task from the list of tasks
    if event == "Remove Task":
        selected = values["tasks"][0]
        tasks.remove(selected)
        window["tasks"].update(values=tasks)

# Close the window
window.close()

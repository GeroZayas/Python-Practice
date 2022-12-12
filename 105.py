import PySimpleGUI as sg

# create an empty list to store to-do items
tasks = []

# main layout of the app
layout = [
    [sg.Text("Tasks")],
    [sg.Listbox(values=tasks, size=(40, 10), key="tasks_list")],
    [sg.Input(key="new_task")],
    [sg.Button("Add"), sg.Button("Complete"), sg.Button("Quit")]
]

# create the window
window = sg.Window("To-Do App").Layout(layout)

# main loop of the app
while True:
    event, values = window.Read()

    # add a new task
    if event == "Add":
        task = values["new_task"]
        tasks.append(task)
        # update the listbox with the new task
        window.FindElement("tasks_list").Update(values=tasks)

    # mark a task as complete
    elif event == "Complete":
        # get the selected task
        selected = values["tasks_list"][0]
        if selected:
            # mark the task as completed
            tasks[tasks.index(selected)] = "[COMPLETED] " + selected
            # update the listbox
            window.FindElement("tasks_list").Update(values=tasks)

    # quit the app
    elif event == "Quit":
        break

# close the window
window.Close()

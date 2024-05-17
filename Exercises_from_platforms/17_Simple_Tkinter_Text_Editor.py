#  Build A Text Editor - Python Tkinter GUI Inspired by Codemy.com

from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Gero's Text Editor")
# root.iconbitmap("./text.ico")
root.geometry("1200x660")

# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False


# # # FUNCTIONS -------------------------


# Open Popup Box when we perform a command
def open_popup(action, message):
    top = Toplevel(root)
    x = len(message) * 10 + 30
    y = 70
    top.geometry(f"{x}x{y}")
    top.title(f"{action}")
    Label(top, text=message, font=("Helvetica", 16)).place(x=10, y=20)


# Create new file function
def new_file():
    my_text.delete("1.0", END)  # first line is 1.0 and the last one is END
    # Update status bars
    root.title("New File - TextPad!")
    status_bar.config(text="New File        ")
    global open_status_name
    open_status_name = False


# Open file function
def open_file():
    # Delete previous text
    my_text.delete("1.0", END)  # first line is 1.0 and the last one is END

    # Grab file name
    text_file = filedialog.askopenfilename(
        initialdir="./",
        title="Open File",
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Python Files", "*.py"),
            ("All files", "*.*"),
        ),
    )

    # check to see if there's a file name
    if text_file:
        # make filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    # Update the Status bars
    name = text_file
    status_bar.config(text=f"{name}        ")
    name = name.replace(
        "C:/Users/Gero Zayas/Downloads/CODING/0 GERO PYTHON/2022/03 Marzo/05 marzo 2022/",
        "",
    )
    root.title(f"{name} - TextPad!")

    # Open the file
    text_file = open(text_file, "r")
    stuff = text_file.read()

    # Add file to textbox
    my_text.insert(END, stuff)

    # Close the opened filed
    text_file.close()


def save_as_file():
    text_file = filedialog.asksaveasfilename(
        defaultextension=".*",
        initialdir="./",
        title="Save file",
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Python Files", "*.py"),
            ("All files", "*.*"),
        ),
    )
    if text_file:
        # update status bar
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace(
            "C:/Users/Gero Zayas/Downloads/CODING/0 GERO PYTHON/2022/03 Marzo/05 marzo 2022/",
            "",
        )
        root.title(f"{name} - TextPad!")

        # Save the file
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

        # put status update or popup code
        open_popup("Saved file", f"Saved as {name}")


# Save file function
def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

        status_bar.config(text=f"Saved: {open_status_name}        ")
    else:
        save_as_file()


# Cut text
def cut_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:  # if there's an event
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab selected text from text box
            selected = my_text.selection_get()
            # Delete selected text from text box
            my_text.delete("sel.first", "sel.last")
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copy text
def copy_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:  # if there's an event
        selected = root.clipboard_get()
    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get()
        # Clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)


# Paste text
def paste_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:  # if there's an event
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


# Create a main frame
my_frame = Frame(root)
my_frame.pack(pady=5)
# Create a Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create text box
my_text = Text(
    my_frame,
    width=97,
    height=25,
    font=("Helvetica", 16),
    selectbackground="yellow",
    selectforeground="black",
    undo=True,
    yscrollcommand=text_scroll.set,
)
my_text.pack()

# Configure the Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu

my_menu = Menu(root)
root.config(menu=my_menu)

# add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(
    label="Cut", command=lambda: cut_text(False), accelerator="(Control + x)"
)
edit_menu.add_command(
    label="Copy", command=lambda: copy_text(False), accelerator="(Control + c)"
)
edit_menu.add_command(
    label="Paste             ",
    command=lambda: paste_text(False),
    accelerator="(Control + v)",
)
edit_menu.add_separator()
edit_menu.add_command(
    label="Undo", command=my_text.edit_undo, accelerator="(Control+z)"
)
edit_menu.add_command(
    label="Redo", command=my_text.edit_redo, accelerator="(Control+y)"
)

# Add Status Bar to bottom of App
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop()

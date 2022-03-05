#  Build A Text Editor - Python Tkinter GUI Inspired by Codemy.com

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Gero's Text Editor")
root.iconbitmap("./text.ico")
root.geometry("1200x660")


# Create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title('New File - TextPad!')
    status_bar.config(text="New File        ")

# Create a main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create a Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create text box
my_text = Text(
    my_frame, width=97, height=25, font=("Helvetica", 16),
    selectbackground="yellow", selectforeground="black", undo=True,
    yscrollcommand=text_scroll.set)
my_text.pack()

# Configure the Scrollbar
text_scroll.config(command=my_text.yview)

# Create Menu

my_menu = Menu(root)
root.config(menu=my_menu)

# add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar to bottom of App
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()

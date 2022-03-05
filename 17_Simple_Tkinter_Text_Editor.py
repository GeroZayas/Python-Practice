#  Build A Text Editor - Python Tkinter GUI Inspired by Codemy.com

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Gero Zayas Text Editor")
root.iconbitmap("./text.ico")
root.geometry("1200x660")

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
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command()

root.mainloop()

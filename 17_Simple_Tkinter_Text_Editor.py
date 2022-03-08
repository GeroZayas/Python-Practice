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
    my_text.delete("1.0", END)  # first line is 1.0 and the last one is END
    # Update status bars
    root.title('New File - TextPad!')
    status_bar.config(text="New File        ")


# Open file function
def open_file():
    # Delete previous text
    my_text.delete("1.0", END)  # first line is 1.0 and the last one is END

    # Grab file name
    text_file = filedialog.askopenfilename(
        initialdir="./",
        title="Open File",
        filetypes=(("Text Files", "*.txt"),
                   ("HTML Files", "*.html"),
                   ("Python Files", "*.py"),
                   ("All files", "*.*")))
    # Update the Status bars
    name = text_file
    status_bar.config(text=f"{name}        ")
    name = name.replace("C:/Users/Gero Zayas/Downloads/CODING/0 GERO PYTHON/2022/03 Marzo/05 marzo 2022/", '')
    root.title(f'{name} - TextPad!')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    # Add file to textbox
    my_text.insert(END, stuff)

    # Close the opened filed
    text_file.close()


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*',
                                             initialdir="./",
                                             title="Save file",
                                             filetypes=(("Text Files", "*.txt"),
                                                        ("HTML Files", "*.html"),
                                                        ("Python Files", "*.py"),
                                                        ("All files", "*.*")))
    if text_file:
        # update status bar
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace("C:/Users/Gero Zayas/Downloads/CODING/0 GERO PYTHON/2022/03 Marzo/05 marzo 2022/", '')
        root.title(f"{name} - TextPad!")

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()
        
# Save file function
def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()
        status_bar.config(text=f"Saved: {open_status_name}        ")
    else:
        save_as_file()


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
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as", command=save_as_file)
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

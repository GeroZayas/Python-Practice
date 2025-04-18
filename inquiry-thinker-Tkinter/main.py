from tkinter import *
from tkinter import ttk


def add_label():
    return ttk.Label(frm, text="I am another label!").grid(column=2, row=3)

root = Tk()
root.geometry("500x600")
root.title("Gero Zayas")
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm, text="Hello Worlds!").grid(column=10, row=0)
ttk.Button(frm, text="Quit", command=add_label).grid(column=2, row=1)
# Create the label widget with all options
text_var= "HELLO MAN!!"
label = ttk.Label(root,
                 textvariable=text_var,
                 width=30,
                 font=("Arial", 16, "bold"),
                 cursor="hand2",
                 underline=0,
                 wraplength=250
                )
root.mainloop()



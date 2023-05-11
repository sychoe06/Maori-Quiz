"""Component 1 - Start Quiz (version 2)
New Window displayed when start button is clicked
"""
# This will import all the widgets and modules which are available in
# tkinter and ttk module
from tkinter import *

root = Tk()
root.title("Maori Quiz")


def start_quiz():
    # Toplevel object which will be treated as a new window
    new_window = Toplevel(root)

    # sets the title of the Toplevel widget
    new_window.title("New Window")

    # sets the geometry of toplevel
    new_window.geometry("200x200")

    # A Label widget to show in toplevel
    Label(new_window, text="This is a new window").pack()


root.minsize(900, 600)  # sets minimum resizeable dimensions
root.maxsize(1000, 700)

# Intro to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black")
welcome_lbl.pack(pady=10)

Maori_Quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red")
Maori_Quiz_lbl.pack(pady=10)

# Start button
start_btn = Button(root, text="START", command=start_quiz,
                   font=("Calibri", 20, "bold"), fg="white", bg="black")
start_btn.pack(pady=10)

# Setting position
welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
Maori_Quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()

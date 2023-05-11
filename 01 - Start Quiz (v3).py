"""Component 1 - Start Quiz (version 3)
Button added
"""

from tkinter import *

root = Tk()
root.title("Maori Quiz")
root.minsize(900, 600)  # sets minimum resizeable dimensions
root.maxsize(1000, 700)

# Intro to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black", bg="white")
Maori_Quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red", bg="white")
welcome_lbl.pack()
Maori_Quiz_lbl.pack()

# Start button
start_btn = Button(root, text="START", fg="white", bg="black")
start_btn.pack()

root.mainloop()

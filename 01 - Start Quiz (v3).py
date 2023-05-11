"""Component 1 - Start Quiz (version 2)
Create function for starting the quiz that will be triggered when start button
is clicked
"""

from tkinter import *


def start_quiz():
    print("start")
    # Hides the labels and buttons to display blank screen
    welcome_lbl.pack_forget()
    Maori_Quiz_lbl.pack_forget()


root = Tk()
root.title("Maori Quiz")
root.minsize(900, 600)  # sets minimum resizeable dimensions
root.maxsize(1000, 700)

# Intro to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black")
welcome_lbl.pack()

Maori_Quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red")
Maori_Quiz_lbl.pack()

# Start button
start_btn = Button(root, text="START", command=start_quiz(),
                   font=("Calibri", 20, "bold"), fg="white", bg="black")
start_btn.pack()

# Setting position
welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
Maori_Quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()

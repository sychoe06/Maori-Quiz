"""Component 2 - Questions (version 1)
Display "Question 1" and the question below when new window is opened
"""
from tkinter import *

root = Tk()


# Launches Maori Quiz
def start_quiz():
    root.destroy()  # Deletes the starting window
    # New Window is created using Tk class
    new = Tk()
    new.title("Maori Quiz")  # Sets title for new window

    new.geometry("900x600")  # Sets dimensions
    question_lbl = Label(new, text="What is the colour red in Maori")
    question_lbl.pack()
    new.mainloop()


root.title("Maori Quiz")  # Sets title for window
root.geometry("900x600")  # Sets dimensions for window

# Intro to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black")

Maori_Quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red")

# Start button - activates quiz when clicked
start_btn = Button(root, text="START", command=start_quiz,
                   font=("Calibri", 20, "bold"), fg="white", bg="black")

# Setting position - centering labels and button
welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
Maori_Quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()

"""Component 1 - Start Quiz (version 1)
New blank window displayed when start button is clicked
"""
from tkinter import *

root = Tk()


# Starts Maori Quiz
def start_quiz():
    # Toplevel object which will be treated as a new window
    new = Toplevel(root)

    # sets the title of the Toplevel widget
    new.title("New Window")

    # sets the geometry of toplevel
    new.geometry("900x600")  # Sets dimensions for window


root.title("Maori Quiz")  # Sets title for window
root.geometry("900x600")  # Sets dimensions for window

# Intro to welcome user
welcome_lbl = Label(root, text="Welcome to the",
                    font=("Calibri", 20, "bold"), fg="black")

main_quiz_lbl = Label(root, text="Maori Quiz",
                       font=("Calibri", 50, "bold"), fg="red")

# Start button - activates quiz when clicked
start_btn = Button(root, text="START", command=start_quiz,
                   font=("Calibri", 20, "bold"), fg="white", bg="black")

# Setting position - centering labels and button
welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
main_quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()

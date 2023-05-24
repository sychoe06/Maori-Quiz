"""Component 2 - Questions (version 2) - Trial Two
Uses a function to create another question when called
"""
from tkinter import *

root = Tk()


# Intro window to start the quiz
def intro():
    root.title("Maori Quiz - Start")  # Sets title for window
    root.geometry("900x600")  # Sets dimensions for window

    # Intro to welcome user
    welcome_lbl = Label(root, text="Welcome to the",
                        font=("Calibri", 20, "bold"), fg="black")
    maori_quiz_lbl = Label(root, text="Maori Quiz",
                           font=("Calibri", 50, "bold"), fg="red")

    # Start button - activates quiz when clicked
    start_btn = Button(root, text="START", command=start_quiz,
                       font=("Calibri", 20, "bold"), fg="white", bg="black")

    # Setting position - centering labels and button
    welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
    maori_quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    root.mainloop()


# Starts Maori Quiz
def start_quiz():
    root.destroy()  # Deletes the starting window

    # New Window is created using Tk class
    win = Tk()
    win.title("Maori Quiz")  # Sets title for new window
    win.geometry("900x600")  # Sets dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=900, height=100, bg="red")

    # Add the name "Maori Quiz" in Canvas
    quiz_name.create_text(450, 50, text="Maori Quiz", fill="white",
                          font=("Calibri", 30, "bold"))
    quiz_name.pack()

    # Displays question
    display_question(win, 1)  # Question 1

    win.mainloop()


def display_question(parent, q_num):
    questions_list = [(1, "Q1: What is red in Maori?")]
    for qt in questions_list:
        if qt[0] == q_num:
            question = f"{qt[1]}"
            # Creates label for question
            question_lbl = Label(parent, text=question, font=("Calibri", 25))
            question_lbl.place(relx=0.06, rely=0.25, anchor=NW)


# Main Routine
intro()

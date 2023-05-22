"""Component 2 - Questions (version 3) - Trial Three
Uses a function to change the text in the question label when called
"""
from tkinter import *

root = Tk()


# Intro window to start the quiz
def intro():
    root.title("Maori Quiz")  # Sets title for window
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

    # Sets up template for question label
    question_lbl = Label(win, text="", font=("Calibri", 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    change_question(question_lbl, 1)  # Displays Question 1

    win.mainloop()


def change_question(label, q_num):
    questions_list = [(1, "Q1: What is red in Maori?")]
    for qt in questions_list:
        if qt[0] == q_num:
            question = f"{qt[1]}"
            # Changes the text in the question label
            label.config(text=question)


# Main Routine
intro()

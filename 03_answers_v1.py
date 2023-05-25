"""Component 3 - Answers (version 1) - Trial One
Using pack() to display the option buttons below question
"""
from tkinter import *

root = Tk()
questions_list = [(1, "Q1: What is red in Maori?", "Whero")]
options_list = [(1, "Whero", "Kowhai", "Ma")]


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

    # Sets up template for question label
    question_lbl = Label(win, text="", font=("Calibri", 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    change_question(question_lbl, 1)  # Displays Question 1
    setup_options(win, 1)

    # Sets up options for question

    win.mainloop()


# Changes the text in the question label
def change_question(lbl, q_num):
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            question = f"{qt[1]}"
            # Changes the text in the question label
            lbl.config(text=question)


# Sets up options for each question
def setup_options(parent, q_num):
    for opts in options_list:
        if opts[0] == q_num:
            opt1 = opts[1]  # Option 1
            display_options(parent, opt1)  # calls function to display

            opt2 = opts[2]  # Option 2
            display_options(parent, opt2)  # calls function to display

            opt3 = opts[3]  # Option 3
            display_options(parent, opt3)  # calls function to display


# Displays options as buttons
def display_options(parent, opt_text):
    opt_btn = Button(parent, text=opt_text, font=("Calibri", 25),
                     width=10, fg="white", bg="black")
    opt_btn.pack(padx=60, side=LEFT)  # Sets position of button using pack()


# Main Routine
intro()

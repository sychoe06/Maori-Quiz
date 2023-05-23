"""Component 4 - Main Loop (version 1)
Sets min and max size for window, Adds all questions and options to their lists
Displays a "next" button at the bottom
"""
from tkinter import *

root = Tk()

# Setup lists to hold questions, answers and options
questions_list = [(1, "Q1: What is red in Maori?", "Whero"),
                  (2, "Q2: What is three in Maori?", "Toru"),
                  (3, "Q3: What is Sunday in Maori?", "Ratapu"),
                  (4, "Q4: What is green in Maori?", "Kakariki"),
                  (5, "Q5: What is 10 in Maori?", "Tekau"),
                  (6, "Q6: What is Thursday in Maori?", "Rapare")]
options_list = [(1, "Whero", "Kowhai", "Ma"), (2, "Tahi", "rima", "Toru"),
                (3, "Ratapu", "Ramere", "Rahori"),
                (4, "Karaka", "Kakariki", "Kowhai"), (5, "")]

# Set up variables
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for all buttons
Q_FONT = "Calibri"  # Quiz Font


# Intro window to start the quiz
def intro():
    root.title(QUIZ_NAME)  # Sets title for window
    root.geometry("900x600")  # Sets dimensions for window

    # Intro to welcome user
    welcome_lbl = Label(root, text="Welcome to the",
                        font=(Q_FONT, 20, "bold"), fg="black")
    maori_quiz_lbl = Label(root, text=QUIZ_NAME,
                           font=(Q_FONT, 50, "bold"), fg="red")

    # Start button - activates quiz when clicked
    start_btn = Button(root, text="START", font=(Q_FONT, BTN_SIZE, "bold"),
                       bg=BLACK, fg=WHITE, command=start_quiz)

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
    win.title(QUIZ_NAME)  # Sets title for new window
    win.geometry("900x600")  # Sets dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=900, height=100, bg=RED)

    # Add the name "Maori Quiz" in Canvas
    quiz_name.create_text(450, 50, text=QUIZ_NAME, fill=WHITE,
                          font=(Q_FONT, 30, "bold"))
    quiz_name.pack()

    # Sets up template for question label
    question_lbl = Label(win, text="", font=(Q_FONT, 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    change_question(question_lbl, 1)  # Displays Question 1
    display_options(win, 1)  # Displays

    #
    win.mainloop()


# Changes the text in the question label
def change_question(lbl, q_num):
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            # Changes the text in the question label
            lbl.config(text=qt[1])


# Displays options for each question
def display_options(master, q_num):
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            opt1 = Button(master, text=opts[1], font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_answer(opts[1], master, 50, opt1, opt2, opt3))
            opt1.place(x=50, y=300)

            opt2 = Button(master, text=opts[2], font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_answer(opts[2], master, 350, opt1, opt2, opt3))
            opt2.place(x=350, y=300)

            opt3 = Button(master, text=opts[3], font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_answer(opts[3], master, 650, opt1, opt2, opt3))
            opt3.place(x=650, y=300)


# Checks if selected option is correct answer
def check_answer(selected_opt, master, opt_x, btn1, btn2, btn3):
    for answer in questions_list:
        if selected_opt == answer[2]:
            correct_lbl = Label(master, text="Correct!", font=(Q_FONT, 20),
                                fg=GREEN)
            correct_lbl.place(x=opt_x, y=400)
        else:
            incorrect_lbl = Label(master, text="Incorrect!",
                                  font=(Q_FONT, 20), fg=RED)
            incorrect_lbl.place(x=opt_x, y=400)

        btn1.config(state="disabled")
        btn2.config(state="disabled")
        btn3.config(state="disabled")


# Main Routine
intro()

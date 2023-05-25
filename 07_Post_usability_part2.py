"""Post Usability testing 1 - Show correct answer (version 3)
Add more questions to make quiz longer - edited to only show start quiz window
"""
from tkinter import *
from tkinter import messagebox

# Setup lists to hold questions, answers and options
questions_list = [(1, "red", "Whero"), (2, "3", "Toru"),
                  (3, "Sunday", "Ratapu"), (4, "10", "Tekau"),
                  (5, "green", "Kakariki"), (6, "Thursday", "Rapare"),
                  (7, "6", "Ono"), (8, "brown", "Parauri"),
                  (9, "Monday", "Rahina"), (10, "8", "Waru")]
options_list = [(1, "Whero", "Kowhai", "Ma"), (2, "Tahi", "Rima", "Toru"),
                (3, "Ratapu", "Ramere", "Rahori"), (4, "Waru", "Rua", "Tekau"),
                (5, "Karaka", "Kakariki", "Kowhai"),
                (6, "Raapa", "Ratu", "Rapare"), (7, "Iwa", "Ono", "Wha"),
                (8, "Kikorangi", "Parauri", "Mangu"),
                (9, "Rahina", "Ramere", "Ratu"), (10, "Whitu", "Rima", "Waru")]


# Set up constants
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"
LIGHT_GREEN = "#8AC847"
LIGHT_RED = "#ffcccb"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

# Set up variables
q_num = 0  # Sets question number
score = 0  # Sets user's score
total_num_qt = 6  # Total number of questions


# Starts Maori Quiz window
def start_quiz():
    global q_num
    q_num = 0  # Resets question number to 0 when quiz starts
    global score
    score = 0  # Resets score to 0 when quiz starts

    # root.withdraw()  # Hides the intro window

    # New Window is created using Tk class
    win = Tk()
    win.deiconify()  # Redraws the start quiz window if it has been withdrawn

    win.title(QUIZ_NAME)  # Sets title for new window
    win.geometry(DIMENSIONS)  # Sets dimensions
    win.maxsize(WIDTH, HEIGHT)  # Sets maximum dimensions
    win.minsize(850, 550)  # Sets minimum dimensions

    # Create a canvas object
    quiz_name = Canvas(win, width=900, height=100, bg=RED)

    # Add the name "Maori Quiz" in Canvas
    quiz_name.create_text(450, 50, text=QUIZ_NAME, fill=WHITE,
                          font=(Q_FONT, 30, "bold"))
    quiz_name.pack()

    # Sets up template for question label
    question_lbl = Label(win, text="", font=(Q_FONT, 25))
    question_lbl.place(relx=0.06, rely=0.25, anchor=NW)

    # Calls function to change text in question
    change_question(win, question_lbl)

    q_status = "not answered"  # Option hasn't been selected yet
    next_button(win, question_lbl, q_status)  # Calls next button function

    win.mainloop()


# Displays options for each question
def display_options(main, lbl):
    global q_num
    for opts in options_list:
        # If the question number matches with the options for that question
        # Then display those options as buttons
        if opts[0] == q_num:
            # Option 1 button
            opt1_txt = opts[1]  # Sets a variable for option 1
            opt1 = Button(main, text=opt1_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt1, opt1_txt, 50))
            opt1.place(x=50, y=300)

            # Option 2 button
            opt2_txt = opts[2]  # Sets a variable for option 2
            opt2 = Button(main, text=opt2_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt2, opt2_txt, 350))
            opt2.place(x=350, y=300)

            # Option 3 button
            opt3_txt = opts[3]  # Sets a variable for option 3
            opt3 = Button(main, text=opt3_txt, font=(Q_FONT, BTN_SIZE),
                          width=10, fg=WHITE, bg=BLACK, command=lambda:
                          check_opt(opt3, opt3_txt, 650))
            opt3.place(x=650, y=300)

    # Checks if selected option is correct answer
    def check_opt(opt_btn, selected_opt, opt_x):
        result_lbl = Label(main, text="", font=(Q_FONT, 20))
        result_lbl.place(x=opt_x, y=400)
        for answer in questions_list:
            if answer[0] == q_num:
                # If selected option is the answer, display "correct!"
                if selected_opt == answer[2]:
                    result_lbl.config(text="Correct!", fg=GREEN)
                    opt_btn.config(fg=BLACK, bg=LIGHT_GREEN)

                    add_score()  # Adds to score

                # If selected option is not the answer, display "incorrect!"
                else:
                    result_lbl.config(text="Incorrect!", fg=RED)
                    opt_btn.config(fg=BLACK, bg=LIGHT_RED)

                # Disables all buttons so only one option is selected at a time
                opt1.config(state="disabled")
                opt2.config(state="disabled")
                opt3.config(state="disabled")
                main.after(500, result_lbl.destroy)
        # Next button can be clicked now
        next_button(main, lbl, "answered")

    # Keeps record of user's score - number of questions correct
    def add_score():
        global score
        score += 1  # Increases score by one when this function is called


# Displays Next button to go to next question
def next_button(main, qt_lbl, qt_status):
    global q_num
    next_btn = Button(main, text="Next", font=(Q_FONT, 20), fg=WHITE, bg=GREEN)
    next_btn.place(x=750, y=450)
    # If the question has been answered - option is selected
    if qt_status == "answered":
        # Then allow user to click "next" to go to next question
        next_btn.config(command=lambda: change_question(main, qt_lbl))
    else:
        # If not then display error message
        next_btn.config(command=msg_error)


# Error message for "next" button
def msg_error():
    messagebox.showerror("Error", "Please select your answer before going to "
                                  "the next question")


# Changes the text in the question label
def change_question(main, lbl):
    global q_num
    q_num += 1  # Question number increases every time "next" button is clicked
    next_button(main, lbl, "not answered")
    # Searches question in question list
    for qt in questions_list:
        if qt[0] == q_num:  # If it is question one
            # Changes the text in the question label
            lbl.config(text=f"Q{q_num}: What is {qt[1]} in Maori?")

    display_options(main, lbl)  # Calls function to display options


# Main routine
start_quiz()

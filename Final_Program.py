"""Final Working Program - Maori Quiz program
This is the Maori Quiz program that tests your knowledge on Te Reo Maori
"""
from tkinter import *
from tkinter import messagebox


class Quiz:
    def __init__(self, s1, qt, opt1, opt2, opt3, qt_num):
        global score
        score = 0
        self.s1 = s1
        f1 = Frame(self.s1)
        f1.pack()

        # Question label
        self.question = Label(s1, text=qt, font=(Q_FONT, 25))
        self.question.place(relx=0.06, rely=0.25, anchor=NW)

        # Option 1 button
        self.b1 = Button(s1, text=opt1, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt1, self.b1, 50))
        self.b1.place(x=50, y=300)
        change_on_hover(self.b1, GREY, BLACK)  # changes hover colour

        # Option 2 button
        self.b2 = Button(s1, text=opt2, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt2, self.b2, 350),)
        self.b2.place(x=350, y=300)
        change_on_hover(self.b2, GREY, BLACK)  # changes hover colour

        # Option 3 button
        self.b3 = Button(s1, text=opt3, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt3, self.b3, 650),)
        self.b3.place(x=650, y=300)
        change_on_hover(self.b3, GREY, BLACK)  # changes hover colour

        # "Next" button - display next question
        self.next_btn = Button(s1, text="NEXT", font=(Q_FONT, 20), fg=WHITE,
                               bg=GREEN, width=7, command=self.next_qt)
        self.next_btn.place(x=720, y=480)
        change_on_hover(self.next_btn, LIGHT_GREEN, GREEN)  # changes hover colour

        self.qt_num = qt_num  # Question number
        self.result = Label(s1, font=(Q_FONT, 20))
        self.correct = Label(s1, font=(Q_FONT, 20), fg=GREEN, bg=LIGHT_GREEN)
        self.answered = False

        self.question_progress()

    # Checks if the selection option is correct or incorrect
    def check(self, selected_opt, opt_btn, opt_x):
        global score
        self.answered = True
        for a in answers_list:
            if a[0] == self.qt_num:
                # If the selected option matches the answer
                if selected_opt == a[1]:
                    # Then display "correct!"
                    self.result.config(text="Correct!", fg=GREEN)
                    opt_btn.config(bg=LIGHT_GREEN)  # button changes to green
                    btn_colour = LIGHT_GREEN
                    score += 1
                # If the selected option doesn't match the answer
                else:
                    # Then display "incorrect" and the correct answer
                    self.result.config(text="Incorrect!", fg=RED)
                    opt_btn.config(bg=LIGHT_RED)  # button changes to red
                    btn_colour = LIGHT_RED
                    self.correct.config(text=f"{a[1]} is the correct answer!")
                    self.correct.place(relx=0.06, rely=0.35, anchor=NW)

                self.result.place(x=opt_x, y=400, anchor=W)

                disable_btn(self.b1)
                disable_btn(self.b2)
                disable_btn(self.b3)

                # Button colour no longer changes on hover because its disabled
                if self.b1 == opt_btn:
                    # Change selected option button to stay light green or red
                    change_on_hover(self.b1, btn_colour, btn_colour)
                    # Keep other option buttons black
                    change_on_hover(self.b2, BLACK, BLACK)
                    change_on_hover(self.b3, BLACK, BLACK)
                elif self.b2 == opt_btn:
                    change_on_hover(self.b2, btn_colour, btn_colour)
                    change_on_hover(self.b1, BLACK, BLACK)
                    change_on_hover(self.b3, BLACK, BLACK)
                else:
                    change_on_hover(self.b3, btn_colour, btn_colour)
                    change_on_hover(self.b1, BLACK, BLACK)
                    change_on_hover(self.b2, BLACK, BLACK)

    # Changes the button's text and command
    def change_btn(self, btn, opt, opt_x):
        btn.config(text=opt, bg=BLACK, command=lambda: self.check(opt, btn,
                                                                  opt_x))
        change_on_hover(btn, GREY, BLACK)

    # Displays the next question and options
    def next_qt(self):
        # If the question has been answered then go to next question
        if self.answered is True:
            # Hides labels from the "check" method
            self.result.place_forget()
            self.correct.place_forget()
            self.qt_num += 1  # Increase the question number by 1
            self.question_progress()

            for qt in questions_list:
                if qt[0] == self.qt_num:
                    # Enable all the option buttons
                    enable_btn(self.b1)
                    enable_btn(self.b2)
                    enable_btn(self.b3)
                    # Change to next question
                    self.question.config(text=qt[1])
                    # Change options for next question
                    opt1 = qt[2]
                    opt2 = qt[3]
                    opt3 = qt[4]
                    self.change_btn(self.b1, opt1, 50)
                    self.change_btn(self.b2, opt2, 350)
                    self.change_btn(self.b3, opt3, 650)
            self.answered = False  # This new question has not been answered

            if self.qt_num > total_num_qt:
                end_quiz(self.s1)

        # If the question hasn't been answered then don't go to next question
        else:
            msg_error()  # Display an error to the user instead

    # Shows how many questions the user has done out of 10
    def question_progress(self):
        qt_progress = Label(self.s1, font=(Q_FONT, 15), fg=GREY,
                            text=f"Question {self.qt_num}/{total_num_qt}")
        qt_progress.place(relx=0.92, rely=0.28, anchor=NE)


# Intro window to start the quiz
def intro():
    root.deiconify()  # Redraws the intro window if it has been withdrawn

    root.title(f"{QUIZ_NAME} - Start")  # Sets title for window
    root.geometry(DIMENSIONS)  # Sets dimensions for window
    root.maxsize(WIDTH, HEIGHT)  # Sets maximum dimensions

    # Intro to welcome user
    welcome_lbl = Label(root, text="Welcome to the",
                        font=(Q_FONT, 20, "bold"), fg="black")
    maori_quiz_lbl = Label(root, text=QUIZ_NAME,
                           font=(Q_FONT, 50, "bold"), fg="red")

    # Start button - activates quiz when clicked
    start_btn = Button(root, text="START", font=(Q_FONT, BTN_SIZE, "bold"),
                       bg=BLACK, fg=WHITE, command=start_quiz)
    change_on_hover(start_btn, GREY, BLACK)  # changes hover colour

    # Setting position - centering labels and button
    welcome_lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
    maori_quiz_lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
    start_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    root.mainloop()


def start_quiz():
    root.withdraw()  # Hides the intro window

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

    q_num = 1  # Sets question number to 1
    for qt in questions_list:
        if qt[0] == q_num:
            Quiz(win, qt[1], qt[2], qt[3], qt[4], q_num)

    win.mainloop()


def end_quiz(win):
    global score
    win.withdraw()  # Hides the start quiz window

    end = Tk()
    end.deiconify()  # Redraws the end window if it has been withdrawn
    # New Window is created using Tk class for the end of the quiz
    end.title(f"{QUIZ_NAME} - End")  # Sets title for new window
    end.geometry(DIMENSIONS)  # Sets dimensions
    end.maxsize(WIDTH, HEIGHT)  # Sets maxsize for window

    # Create a canvas object
    finished_quiz = Canvas(end, width=WIDTH, height=100, bg=RED)

    # Add the name "Maori Quiz" in Canvas
    finished_quiz.create_text(450, 50, fill=WHITE, font=(Q_FONT, 30, "bold"),
                              text="Congrats! You have finished the quiz!")
    finished_quiz.pack()

    # Score labels created
    score_lbl = Label(end, text="Your score is...", font=(Q_FONT, 20))
    score_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)
    user_score_lbl = Label(end, text=f"{score}/{total_num_qt}",
                           font=(Q_FONT, 80, "bold"), fg=GREEN)
    user_score_lbl.place(relx=0.5, rely=0.45, anchor=CENTER)

    # Play again button
    play_again_btn = Button(end, text="PLAY AGAIN", font=(Q_FONT, BTN_SIZE),
                            fg=WHITE, bg=BLACK, width=15,
                            command=lambda: again(end))
    play_again_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
    change_on_hover(play_again_btn, GREY, BLACK)  # changes hover colour

    # Exit button
    exit_btn = Button(end, text="EXIT", font=(Q_FONT, BTN_SIZE), fg=WHITE,
                      bg=BLACK, width=15, command=lambda: confirm(end))
    exit_btn.place(relx=0.5, rely=0.85, anchor=CENTER)
    change_on_hover(exit_btn, GREY, BLACK)  # changes hover colour


# Disables buttons - doesn't allow buttons to be clicked
def disable_btn(btn):
    btn.config(state="disabled")


# Enables buttons - allows buttons to be clicked
def enable_btn(btn):
    btn.config(state="normal")


# Error message for "next" button
def msg_error():
    messagebox.showerror("Error", "Please select your answer before going to "
                                  "the next question")


# Changes colour of button on hover
def change_on_hover(button, colour_on_hover, colour_on_leave):
    # Colour of button changes when mouse hovers over it
    button.bind("<Enter>", func=lambda e: button.config(
        background=colour_on_hover))

    # Colour of button changes when mouse is not hovering over it
    button.bind("<Leave>", func=lambda e: button.config(
        background=colour_on_leave))


# Confirms if user wants to finish the quiz
def confirm(end_window):
    close = messagebox.askquestion("Confirm close", "Are you sure you want to "
                                                    "exit the Maori Quiz?")
    if close == "yes":
        end_window.destroy()  # Close the end window
        exit()


# This function is called when user wants to play again
def again(end_window):
    end_window.withdraw()  # Hides the end window
    intro()  # Calls the intro window function


# Main routine
# Contains all the questions and its options
questions_list = [(1, "Q1: What is red in Maori?", "Whero", "Kowhai", "Ma"),
                  (2, "Q2: What is 3 in Maori?", "Tahi", "rima", "Toru"),
                  (3, "Q3: What is Sunday in Maori?", "Ratapu", "Ramere",
                   "Rahori"),
                  (4, "Q4: What is 10 in Maori?", "Waru", "Rua", "Tekau"),
                  (5, "Q5: What is green in Maori?", "Karaka", "Kakariki",
                   "Kowhai"),
                  (6, "Q6: What is Thursday in Maori?", "Raapa", "Ratu",
                   "Rapare"),
                  (7, "Q7: What is 6 in Maori?", "Iwa", "Ono", "Wha"),
                  (8, "Q8: What is brown in Maori?", "Kikorangi", "Parauri",
                   "Mangu"),
                  (9, "Q9: What is Monday in Maori?", "Rahina", "Ramere",
                   "Ratu"),
                  (10, "Q10: What is 8 in Maori?", "Whitu", "Rima", "Waru")]

# Contains all the correct answers for each question
answers_list = [(1, "Whero"), (2, "Toru"), (3, "Ratapu"), (4, "Tekau"),
                (5, "Kakariki"), (6, "Rapare"), (7, "Ono"), (8, "Parauri"),
                (9, "Rahina"), (10, "Waru")]

# Set up constants
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"
LIGHT_GREEN = "#8AC847"
LIGHT_RED = "#ffcccb"
GREY = "grey"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

total_num_qt = 10  # Total number of questions
score = 0  # Sets score to 0

# Run the quiz
root = Tk()
intro()

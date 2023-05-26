"""Component 8 - Post Usability testing - show correct answer (version 2)
Only using the code needed for this component - to save time
If the user gets the answer wrong then the correct answer is shown
"""
from tkinter import *
from tkinter import messagebox


class Quiz:
    def __init__(self, s1, qt, opt1, opt2, opt3, qt_num):
        self.s1 = s1
        f1 = Frame(self.s1)
        f1.pack()
        self.qt_num = qt_num  # Question number
        # Question label
        self.question = Label(s1, text=qt, font=(Q_FONT, 25))
        self.question.place(relx=0.06, rely=0.25, anchor=NW)

        # Option 1 button
        self.b1 = Button(s1, text=opt1, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt1, self.b1, 50))
        self.b1.place(x=50, y=300)

        # Option 2 button
        self.b2 = Button(s1, text=opt2, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt2, self.b2, 350),)
        self.b2.place(x=350, y=300)

        # Option 3 button
        self.b3 = Button(s1, text=opt3, font=(Q_FONT, BTN_SIZE),
                         fg=WHITE, bg=BLACK, width=10,
                         command=lambda: self.check(opt3, self.b3, 650),)
        self.b3.place(x=650, y=300)

        # "Next" button - display next question
        self.next_btn = Button(s1, text="NEXT", font=(Q_FONT, 20), fg=WHITE,
                               bg=GREEN, width=7, command=self.next_qt)
        self.next_btn.place(x=720, y=480)

        self.result = Label(s1, font=(Q_FONT, 20))
        self.correct = Label(s1, font=(Q_FONT, 20), fg=GREEN, bg=LIGHT_GREEN)
        self.answered = False

    # Checks if the selection option is correct or incorrect
    def check(self, selected_opt, opt_btn, opt_x):
        self.answered = True
        for a in answers_list:
            if a[0] == self.qt_num:
                # If the selected option matches the answer
                if selected_opt == a[1]:
                    # Then display "correct!"
                    self.result.config(text="Correct!", fg=GREEN)
                    opt_btn.config(bg=LIGHT_GREEN)  # button changes to green
                # If the selected option doesn't match the answer
                else:
                    # Then display "incorrect" and the correct answer
                    self.result.config(text="Incorrect!", fg=RED)
                    opt_btn.config(bg=LIGHT_RED)  # button changes to red
                    self.correct.config(text=f"{a[1]} is the correct answer!")
                    self.correct.place(relx=0.06, rely=0.35, anchor=NW)
            self.result.place(x=opt_x, y=400, anchor=W)
            disable_btn(self.b1)
            disable_btn(self.b2)
            disable_btn(self.b3)

    # Changes the button's text and command
    def change_btn(self, btn, opt, opt_x):
        btn.config(text=opt, bg=BLACK, command=lambda: self.check(opt, btn,
                                                                  opt_x))

    # Displays the next question and options
    def next_qt(self):
        # If the question has been answered then go to next question
        if self.answered is True:
            # Hides labels from the "check" method
            self.result.place_forget()
            self.correct.place_forget()
            self.qt_num += 1  # Increase the question number by 1

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

        # If the question hasn't been answered then don't go to next question
        else:
            msg_error()  # Display an error to the user instead


def start_quiz():
    # New Window is created using Tk class
    win = Tk()
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

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

# Run the quiz
start_quiz()

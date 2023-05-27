"""Post Usability testing 2: Exit button (version 2)
Added a message box that appears to confirm if user wants to exit the quiz
"""
from tkinter import *
from tkinter import messagebox

# Set up constants
WHITE = "white"
BLACK = "black"
RED = "red"
GREEN = "green"

QUIZ_NAME = "Maori Quiz"  # Name of Quiz
BTN_SIZE = 25  # Size for option buttons and start button
Q_FONT = "Calibri"  # Quiz Font
DIMENSIONS = "900x600"  # Dimensions of window
WIDTH = 900  # Height of window
HEIGHT = 600  # Width of window

# Set up variables
score = 0  # Sets user's score
total_num_qt = 6  # Total number of questions


# End Maori Quiz window
def end_quiz():
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

    # Play again Button
    play_again_btn = Button(end, text="PLAY AGAIN", font=(Q_FONT, BTN_SIZE),
                            fg=WHITE, bg=BLACK, width=15)
    play_again_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Exit button
    exit_btn = Button(end, text="EXIT", font=(Q_FONT, BTN_SIZE),
                      fg=WHITE, bg=BLACK, width=15, command=lambda: confirm(end))
    exit_btn.place(relx=0.5, rely=0.85, anchor=CENTER)

    end.mainloop()


def confirm(end_window):
    close = messagebox.askquestion("Confirm close", "Are you sure you want to "
                                                    "exit the Maori Quiz?")
    if close == "yes":
        end_window.destroy()  # Close the end window
        exit()


# Main routine
end_quiz()

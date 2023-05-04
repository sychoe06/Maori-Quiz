"""Component 1 - Start Quiz (version 2)
Changed icon of Tkinter window
"""

import tkinter as tk
root = tk.Tk()

root.title("Maori Quiz")
root.iconphoto(False, tk.PhotoImage(file="quiz_icon_v2.png"))
root.minsize(900, 600)  # sets minimum resizeable dimensions
root.maxsize(1000, 700)


root.mainloop()

# Plan for using class to make "blueprint" for question

# creates class for question
# defines variables for each part of a question label

# class Questions(self)
# self.font = "calibri"
# self.size = 20
# self.qt1 = "What is "
# self.qt2 = " in Maori?"

# def question_lbl(self, qt_word):
# question = self.qt1 + qt_word + self.qt2
# or
# question = f"{self.qt1} {qt_word} {self.qt2}"
# qt = Label(root, text=question, font=(self.font, self.size)
# qt.pack()

# calls this class for every question
# q1 = question_lbl("red")
# q2 = question_lbl("Monday")

####################################

# class Question(self, qt_word)
# self.font = "calibri"
# self.size = 20
# self.qt1 = "What is "
# self.qt2 = " in Maori?"
# self.qt_word = qt_word

# def question_lbl(self, qt_word):
# question = self.qt1 + self.qt_word + self.qt2
# qt = Label(root, text=question, font=(self.font, self.size)
# qt.pack()

# calls this class for every question
# q1 = Questions("red")
# q2 = Questions("Monday")

######################################

# so then it should display question 1 as "What is red in Maori?"
# Question 2 as "What is Monday in Maori?"

import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.attributes('-topmost', 1)
        self.window.attributes('-topmost', 0)

        self.label_score = tkinter.Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white", highlightthickness=0,
                                         justify="right", pady=10)
        self.label_score.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text((CANVAS_WIDTH / 2), (CANVAS_HEIGHT / 2), text="", fill=THEME_COLOR,
                                                     font=FONT, width=(CANVAS_WIDTH-20))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        image_green = tkinter.PhotoImage(file="images/true.png")
        self.button_green = tkinter.Button(image=image_green, highlightthickness=0, command=self.pressing_true_button)
        self.button_green.grid(column=0, row=2)
        image_red = tkinter.PhotoImage(file="images/false.png")
        self.button_red = tkinter.Button(image=image_red, highlightthickness=0, command=self.pressing_wrong_button)
        self.button_red.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.button_green.config(state="disabled")
            self.button_red.config(state="disabled")


    def pressing_true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressing_wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)





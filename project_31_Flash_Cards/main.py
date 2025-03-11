import tkinter
import  random
import pandas
# ---------------------------- CONSTANTS ------------------------------- #
NAME_OF_GAME = "Flash Cards"
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_WIDTH = 800
CANVAS_LENGTH = 526
LANGUAGE_FROM = "French"
LANGUAGE_TO = "English"
TIME_DELAY_BEFORE_SHOWING_ANSWER = 5000
PATH_TO_FRONT_IMAGE = "images/card_front.png"
PATH_TO_BACK_IMAGE = "images/card_back.png"
PATH_TO_ORIGINAL_DATA_TO_LEARN =  "data/french_words.csv"
PATH_TO_REMAINING_DATA_TO_LEARN = "data/words_to_learn.csv"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")
PATH_TO_GREEN_BUTTON_IMAGE = "images/right.png"
PATH_TO_RED_BUTTON_IMAGE = "images/wrong.png"
# ---------------------------- VARIABLES ------------------------------- #
current_card = {}
data_to_learn = {}
# ---------------------------- READ DATA ------------------------------- #
try:
    remaining_data_to_learn = pandas.read_csv(PATH_TO_REMAINING_DATA_TO_LEARN)
except FileNotFoundError:
    original_data_to_learn = pandas.read_csv(PATH_TO_ORIGINAL_DATA_TO_LEARN)
    data_to_learn = original_data_to_learn.to_dict(orient="records")
else:
    data_to_learn = remaining_data_to_learn.to_dict(orient="records")

# ---------------------------- GENERATE NEXT CARD  ------------------------------- #
def next_card_generator():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_to_learn)
    canvas.itemconfig(image_of_card, image=front_image)
    canvas.itemconfig(title_of_card, text=LANGUAGE_FROM, fill="black")
    canvas.itemconfig(card_content, text=current_card[LANGUAGE_FROM], fill="black")
    flip_timer = window.after(TIME_DELAY_BEFORE_SHOWING_ANSWER, func=flip_the_card)

# ---------------------------- Flip the cards  ------------------------------- #
def flip_the_card():
    canvas.itemconfig(image_of_card, image=back_image),
    canvas.itemconfig(title_of_card, text=LANGUAGE_TO, fill="white"),
    canvas.itemconfig(card_content, text=current_card[LANGUAGE_TO], fill="white")

# ---------------------------- REMOVE KNOWN CARDS FROM DICTIONARY ------------------------------- #
def remove_known_data():
    global remaining_data_to_learn
    data_to_learn.remove(current_card)
    remaining_data_to_learn = pandas.DataFrame(data_to_learn)
    remaining_data_to_learn.to_csv(PATH_TO_REMAINING_DATA_TO_LEARN, index=False)
    next_card_generator()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(NAME_OF_GAME)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(TIME_DELAY_BEFORE_SHOWING_ANSWER, func=flip_the_card)

canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_LENGTH, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = tkinter.PhotoImage(file=PATH_TO_FRONT_IMAGE)
back_image = tkinter.PhotoImage(file=PATH_TO_BACK_IMAGE)
image_of_card = canvas.create_image((CANVAS_WIDTH / 2), (CANVAS_LENGTH / 2), image=front_image)
title_of_card = canvas.create_text((CANVAS_WIDTH / 2), (CANVAS_LENGTH / 4), text="", fill="black", font=FONT_1)
card_content = canvas.create_text((CANVAS_WIDTH / 2), (CANVAS_LENGTH / 2), text="", fill="black", font=FONT_2)
canvas.grid(column=0, row=0, columnspan=2)

image_green = tkinter.PhotoImage(file=PATH_TO_GREEN_BUTTON_IMAGE)
button_green = tkinter.Button(image=image_green, highlightthickness=0, command=remove_known_data)
button_green.grid(column=1, row=1)

image_red = tkinter.PhotoImage(file=PATH_TO_RED_BUTTON_IMAGE)
button_red = tkinter.Button(image=image_red, highlightthickness=0, command=next_card_generator)
button_red.grid(column=0, row=1)

next_card_generator()

window.mainloop()

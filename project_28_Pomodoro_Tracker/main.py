import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

def countdown_mechanism(minutes_left, seconds_left=0):
    global timer
    if seconds_left >= 0 and minutes_left >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes_left:02d}:{seconds_left:02d}" )  # will show the remaining time
        if seconds_left == 0 and minutes_left > 0:
            minutes_left -= 1
            seconds_left = 59
        else:
            seconds_left -= 1
        timer = window.after(1000, countdown_mechanism, minutes_left, seconds_left)
    else:
        start_timer()
        if reps % 2 == 0:
            label_check_mark.config(text=("✅" * (reps // 2)), font=(FONT_NAME, 14, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)


def start_timer():
    global reps
    stop_timer()
    reps += 1
    if reps % 8 == 0:
        label_timer.config(text="BREAK", fg=RED)
        countdown_mechanism(minutes_left=LONG_BREAK_MIN)
    elif reps % 2 == 0:
        label_timer.config(text="BREAK", fg=PINK)
        countdown_mechanism(minutes_left=SHORT_BREAK_MIN)
    else:
        label_timer.config(text="WORK", fg=GREEN)
        countdown_mechanism(minutes_left=WORK_MIN)


def stop_timer(minutes_left=0, seconds_left=0):
    global reps, timer
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text=f"{minutes_left:02d}:{seconds_left:02d}" )
    label_check_mark.config(text="")
    label_timer.config(text="Timer", fg=GREEN)
    timer = None

    
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.attributes('-topmost', 1)
window.attributes('-topmost', 0)

label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
label_timer.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 38, "bold")) # will show remaining time
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2, sticky="W")

button_reset = tkinter.Button(text="Reset", command=stop_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

label_check_mark = tkinter.Label(font=(FONT_NAME, 30, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
label_check_mark.grid(column=1, row=3)

window.mainloop()


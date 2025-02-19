import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

label_miles = tkinter.Label(text="Miles", font=("Arial", 16, "bold"))
label_miles.grid(column=2, row=0)
label_miles.config(padx=20, pady=20)

label_km = tkinter.Label(text="Kilometers", font=("Arial", 16, "bold"))
label_km.grid(column=2, row=1)

label_addit_text = tkinter.Label(text="are equal to:", font=("Arial", 16, "bold"))
label_addit_text.grid(column=0, row=1)

converted = 0
label_converted_miles = tkinter.Label(text=f"{converted}", font=("Arial", 16, "bold"))
label_converted_miles.grid(column=1, row=1)

def click_button_to_convert():
    global converted
    try:
        converted = float(user_input.get()) * 1.609344
    except ValueError:
        messagebox.showwarning(title="Value Error", message= "Please enter a number")
    else:
        label_converted_miles.config(text=converted)

button = tkinter.Button(text="CALCULATE", command=click_button_to_convert)
button.grid(column=1, row=2)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

window.mainloop()

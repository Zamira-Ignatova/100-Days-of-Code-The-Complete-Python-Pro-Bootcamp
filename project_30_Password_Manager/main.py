import  tkinter
from tkinter import messagebox
import  random
import pyperclip
import  json

FONT_NAME = "Courier"
EMAIL = ""
password = ""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    [password_list.append(random.choice(letters)) for letter in range(0, random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for symbol in range(0, random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for number in range(0, random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, string=password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # get the information from entries     # and save it to the file
    website = entry_website.get()
    output_password = entry_password.get()
    email_username = entry_email_username.get()
    new_data = {website:
                    {"email": email_username,
                     "password": output_password,
                     }
                }
    if website == "" or output_password == "" or email_username == "":
        messagebox.showwarning("Warning", message="Please fill out all required fields!")
    else:
        try: # with keyword "try" we are checking a possibility of appearing FileNotFoundError
            with open("data.json", "r") as data_file:
                #reading existing json data file
                data = json.load(data_file)
        except FileNotFoundError: #in case there is no json file creating a new json file and write down  the content from new_data variable
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else: #in case there was no FileNotFoundError
            # updating old data with a new_data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data to data.json file
                json.dump(data, data_file, indent=4)
        finally:
            #delete the current info
            entry_website.delete(0, tkinter.END)
            entry_password.delete(0, tkinter.END)
            entry_email_username.delete(0, tkinter.END)

def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_website = entry_website.get()
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message= "The file with saved passwords does not exit")
    else:
        try:
            email_saved = data[search_website]["email"]
            password_saved = data[search_website]["password"]
            messagebox.showinfo(title=f"{search_website}", message=f"Email: {email_saved}\n" f"Password: {password_saved}")
        except KeyError:
            messagebox.showinfo(title=f"{search_website}", message="No details for the website exists")

def copy_password():
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
password_app_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_app_image)
canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website:", font=(FONT_NAME, 16, "bold"))
label_website.grid(column=0, row=1, sticky="W")

label_email_username = tkinter.Label(text="Email/Username:", font=(FONT_NAME, 16, "bold"))
label_email_username.grid(column=0, row=2, sticky="W")

label_password = tkinter.Label(text="Password:", font=(FONT_NAME, 16, "bold"))
label_password.grid(column=0, row=3, sticky="W")

entry_website = tkinter.Entry(width=21)
entry_website.focus()
entry_website.grid(column=1, row=1)

entry_email_username = tkinter.Entry(width=36)
entry_email_username.insert(0, string=EMAIL)
entry_email_username.grid(column=1, row=2, columnspan=2)

entry_password = tkinter.Entry(width=17)
entry_password.grid(column=1, row=3, sticky="W")

button_add = tkinter.Button(text="Add", command=save_data, highlightthickness=0, width=34)
button_add.grid(column=1, row=4, columnspan=2)

button_generate_password = tkinter.Button(text="Generate Password", command=password_generator, width=11)
button_generate_password.grid(column=2, row=3, sticky="W")

button_search = tkinter.Button(text="Search", command=find_password, highlightthickness=0, width=11)
button_search.grid(column=2, row=1)

button_copy_password = tkinter.Button(text="📋", command=copy_password, highlightthickness=0, width=1)
button_copy_password.grid(column=1, row=3, sticky="E")

window.mainloop()

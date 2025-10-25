from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import os

current_path = os.getcwd()
print(current_path)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_Entry.delete(0, END)  # Clear old password
    password_Entry.insert(0, password)
    pyperclip.copy(password)       # Copy to clipboard automatically

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data_button():
    website = webside_Entry.get()
    email = email_username_Entry.get()
    password = password_Entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?"
    )

    if is_ok:
        with open(f"{current_path}/Data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        webside_Entry.delete(0, END)
        password_Entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=f"{current_path}/Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
webside_label = Label(text="Website:")
webside_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
webside_Entry = Entry(width=35)
webside_Entry.focus()
webside_Entry.grid(column=1, row=1, columnspan=2)

email_username_Entry = Entry(width=35)
email_username_Entry.insert(0, "morax.d.gold@gmail.com")
email_username_Entry.grid(column=1, row=2, columnspan=2)

password_Entry = Entry(width=21)
password_Entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data_button)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

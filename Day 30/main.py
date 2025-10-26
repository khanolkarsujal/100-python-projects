# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os

# ---------------------------- PATH SETUP ------------------------------- #
# This gets the folder where this Python file is located.
# It helps find 'logo.png' even if you run the program from another folder.
location = os.getcwd()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random secure password and copies it to clipboard."""

    # Different types of characters to choose from
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!#$%&()*+')

    # Randomly select some letters, numbers, and symbols
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine all parts and shuffle them to make it more random
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join the list into one string (final password)
    password = "".join(password_list)

    # Insert password into entry box and copy to clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves the website, email, and password details into a JSON file."""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Data structure to be stored
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check if website or password box is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    # Try to open and read existing data
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    # If file not found, create a new one
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    # If file exists, update it with new data
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    # Clear entry fields after saving
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Searches for a saved password for a given website."""

    website = website_entry.get()

    # Try reading the file
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for '{website}' exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a canvas for logo
canvas = Canvas(height=200, width=200)
logo_path = os.path.join(location, "logo.png")  # uses your os setup
logo_img = PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")  # default email

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Keep window running
window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for char in range(nr_letters)]
    random_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = random_symbols + random_letters + random_numbers
    random.shuffle(password_list)
    generated_password = ''.join(password_list)
    pyperclip.copy(generated_password)

    password.delete(0, END)
    password.insert(0, generated_password)

    # print(f"Your password is: {generated_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website.get()) == 0 or len(email.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the blanks.")
    else:
        is_ok = messagebox.askokcancel(title=website.get(), message=f"These are the details entered: "
                                                            f"\nEmail: {email.get()}\nPassword:"
                                                            f" {password.get()}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website.get()} | {email.get()} | {password.get()}\n")
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password manager")
window.minsize(height=100, width=200)
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=150, height=150, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(75, 75, image=lock_img)
canvas.grid(row=0, column=0)

# labels
info_label = Label(text="Simple password manager created by Jan Szwagrzyk\n \nFeatures:\n- stores your data locally"
                        "\n- generates random passwords\n- coppies generated password into a clipboard. ", font=("Arial", 12, "bold"))
info_label.grid(row=0, column=1, columnspan=2)

website_label = Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

# entry
website = Entry(width=38)
website.grid(row=1, column=1, columnspan=2)
website.focus()

email = Entry(width=38)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "mckgasiorek17@gmail.com")

password = Entry(width=20)
password.grid(row=3, column=1)

# button
generate = Button(text="Generate password", command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", command=save, width=36)
add.grid(row=4, column=1, columnspan=2)





window.mainloop()
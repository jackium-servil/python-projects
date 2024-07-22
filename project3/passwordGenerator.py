import random
import string
import os
from tkinter import * 

window = Tk()
window.title("Password Generator")
window.config(background="#000")

def generator():
    os.system("cls")
    password = ""
    source = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_length = int(entry.get())
    for x in range(password_length):
        password += random.choice(source)    
    print(f"The password is : {password}")

label = Label(window,
              text="Enter the length of the password: ",
              bg="red",
              fg="green")
entry = Entry(window,
              bg="gray",
              fg="blue")
button = Button(window,
                text="Subimt",
                command=generator)
label.pack()
entry.pack()
button.pack()
window.mainloop()
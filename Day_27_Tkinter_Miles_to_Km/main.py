from tkinter import *


def button_clicked():
    y = int(user_input.get())
    mileage = y * 1.609
    my_label.config(text=f"{mileage}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=100)
window.config(padx=20, pady=10)

# Entry
user_input = Entry(width=15)
user_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Labels
my_label = Label(text="Miles", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=0)

my_label = Label(text="Km", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=1)

my_label = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)

my_label = Label(text=0, font=("Arial", 12, "bold"))
my_label.grid(column=1, row=1)


window.mainloop()

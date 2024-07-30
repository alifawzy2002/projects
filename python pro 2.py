import tkinter as tk
from tkinter import *
import random

def fun():
    x = guess.get()
    if score.get() > 0:
        if x < 1 or x > 50:
            hint.set("Please guess a number between 1 and 50.")
        elif num == x:
            hint.set("Congratulations! YOU WON!!!")
        else:
            score.set(score.get() - 1)
            final_score.set(score.get())
            if num > x:
                hint.set("Your guess was too low: Guess a higher number.")
            else:
                hint.set("Your guess was too high: Guess a lower number.")
    else:
        hint.set("Game Over. You Lost.")

# Initialize the main window
win = tk.Tk()
win.geometry("750x750")
win.title("Python Project")

# Initialize variables
num = random.randint(1, 50)
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

# Set initial values
hint.set("Guess a number between 1 and 50")
score.set(5)
final_score.set(score.get())

# Create GUI elements
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

# Start the main loop
win.mainloop()


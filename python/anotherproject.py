import tkinter as tk
from tkintertemplate import *
window.title("Clicker Game")
x=int(0)
def add_one():
    global x
    x=x+1
    button.config(text=x)
button = tk.Button(
    text=x,
    height=1200,
    width=800,
    command=add_one
)
button.pack()
if __name__ == "__main__":
    window.mainloop()
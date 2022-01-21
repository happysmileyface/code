from tkintertemplate import *
import tkinter as tk
import keyboard
inputs = "[buttons]"
buttondisplay = tk.Label(
    text=inputs,
    font=(25),
)
quitbutton = tk.Button(
    text="Quit",
    command=window.destroy,
)
quitbutton.pack()
buttondisplay.pack()


if keyboard.on_press("r"):
    buttondisplay.configure(text=keyboard.read_key()+" "+inputs)
    inputs = keyboard.read_key()+" "+inputs
window.mainloop()    




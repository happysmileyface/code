from tkintertemplate import *
import tkinter as tk
Width = 1200
Height = 800
global x
x=int(0)
def update_btn_text():
    global x
    x=x+1
    close_button.configure(text=x)
close_button = tk.Button(
    window,
    text=x,
    width=Width,
    height=Height,
    command=update_btn_text)
close_button.pack(expand=True)
window.mainloop()
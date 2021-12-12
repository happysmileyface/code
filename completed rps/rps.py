from tkintertemplate import *
import tkinter as tk
import random
Width = 1000
Height = 600
window.title("Rock, Paper, Scissors")
global p2_input
p2_input = 0
def Lose():
    results.config(text="You Lost")
def Win():
    results.config(text="You Won")
def Draw():
    results.config(text="You Drew")
def Decide(p1_input,p2_input):
    if p1_input == p2_input:
        Draw()
    if p1_input == "S":
        if p2_input == "P":
            Win()
        if p2_input == "R":
            Lose()
    if p1_input == "P":
        if p2_input == "R":
            Win()
        if p2_input == "S":
            Lose()
    if p1_input == "R":
        if p2_input == "S":
            Win()
        if p2_input == "P":
            Lose()
def P2_Input():
    global p2_input
    p2_input = random.choice("RPS")

def Rock():
    global p1_input
    p1_input = "R" 
    P2_Input()
    Decide(p1_input,p2_input)
def Paper():
    global p1_input
    p1_input = "P"
    P2_Input()
    Decide(p1_input,p2_input)
def Scissors():
    global p1_input
    p1_input = "S"
    P2_Input()
    Decide(p1_input,p2_input)

results = tk.Label(
    text="Choose an Option",
    width=20,
    height=8,)
rock = tk.Button(
    text="Rock",
    width=20,
    height=8,
    command=Rock)
paper = tk.Button(
    text="Paper",
    width=20,
    height=8,
    command=Paper)
scissors = tk.Button(
    text="Scissors",
    width=20,
    height=8,
    command=Scissors)

window.resizable(False,False)
results.pack()
rock.pack()
paper.pack()
scissors.pack()
rock.place(x=150,y=200)
paper.place(x=350,y=200)
scissors.place(x=550,y=200)
if __name__ == "__main__":
    window.mainloop()
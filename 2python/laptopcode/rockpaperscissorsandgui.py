from tkintertemplate import *
from newproject import *
import tkinter as tk
Width = 1000
Height = 600

def Rock():
    global p1_input
    p1_input = "R" 
def Paper():
    global p1_input
    p1_input = "P"
def Scissors():
    global p1_input
    p1_input = "S"
#make text(aka a label) for output and results
#these buttons are for each option and give corresponding input for p1
rock = tk.Button(command=Rock)
paper = tk.Button(command=Paper)
scissors = tk.Button(command=Scissors)
if __name__ == "__main__":
    #generate p2_input
    #make a loop for asking for p1_input, generate random input for p2_input,-
    #- and use Decide() to see if you win or not
    window.mainloop()
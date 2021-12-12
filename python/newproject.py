import random
def Lose():
    print("You lost")
    print("-----------")
def Win():
    print("You won")
    print("-----------")
def Draw():
    print("You drawed")
    print("-----------")
def Invalid():
    print('"'+p1_input+'" was not a valid option')
    print("-----------")
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
print("S for Scissors, P for Paper, and R for Rock:")
print("end to end the game")
# will not start main code if used from other code
if __name__ == "__main__":
    while True:
        p1_input = input()
        if p1_input not in ('R','S','P'):
            Invalid()
        if p1_input == "end":
            break
        #code does not generate p2_input if used from other code (because of the if __name__ == "__main__")
        p2_input = random.choice("SPR")
        Decide(p1_input,p2_input)
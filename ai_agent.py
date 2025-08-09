import random
def solve_logic(puzzle):
    #function to solve the puzzles based on id
    if puzzle["id"]==1:
        return "32",True
    elif puzzle["id"]==2:
        return "yes",True
    elif puzzle["id"]==3:
        return "U",True
    elif puzzle["id"]==4:
        return "true",True
    else:
        return "unknown",False
    
def solve_insight(puzzle):
    #random ai guesses
    guesses =["Turn on one switch,wait,turn it off,turn another on, then enter the room to check the bulb and the warmth",
              "A stamp","An echo","The letter'e","No idea","I don't know"]
    guess=random.choice(guesses)
    correct=(guess.lower()==puzzle["answer"].lower())
    return guess,correct

def solve_puzzle(puzzle):
    if puzzle["type"]=="logic":
        return solve_logic(puzzle)
    else:
        return solve_insight(puzzle)
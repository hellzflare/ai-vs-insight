#function for people to interact with the puzzles
import time

def ask_puzzle(puzzle):
    print("\nPuzzle: ")
    print(puzzle["question"])
    start=time.time()
    answer=input("Your answer: ").strip().lower()
    end = time.time()

    correct_answer=puzzle["answer"].lower()
    correct=(answer==correct_answer)
    time_taken=end-start

    if correct:
        print("Correct!")
    else:
        print("Incorrect.The correct answer was:",puzzle["answer"])
    return correct,time_taken
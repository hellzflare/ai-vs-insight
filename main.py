from puzzles import logical_puzzles, insight_puzzles
from ai_agent import solve_puzzle
from human_interface import ask_puzzle

def main():
    print("Welcome to AI Limits simulator")
    human_scores={"logic":0,"insight":0}
    ai_scores = {"logic": 0, "insight": 0}
    total_logic=len(logical_puzzles)
    total_insight=len(insight_puzzles)
    #human attempt at the logical puzzles
    print("Human Logical Puzzles")
    for i in logical_puzzles:
        correct, _=ask_puzzle(i)
        if correct:
            human_scores["logic"]+=1
    #human attempt at the insight puzzles
    print("Human Insight Puzzles")
    for i in insight_puzzles:
        correct, _ =ask_puzzle(i)
        if correct:
            human_scores["insight"]+=1
    #AI attempt at the logical puzzles
    print("AI Logical Puzzles")
    for i in logical_puzzles:
        answer,correct=solve_puzzle(i)
        print(f"AI answers puzzle {i['id']} with '{answer}' -> {'Correct' if correct else 'Incorrect'}")
        if correct:
            ai_scores["logic"]+=1
    #AI attempt at insight puzzles
    print("AI Insight Puzzles")
    for i in insight_puzzles:
        answer,correct=solve_puzzle(i)
        print(f"AI guesses puzzle {i['id']} with '{answer}' -> {'Correct' if correct else 'Incorrect'}")
        if correct:
            ai_scores["insight"]+=1
    #summary of results
    print("Summary")
    print(f"Human solved{human_scores['logic']}/{total_logic} logic puzzles.")
    print(f"Human solved{human_scores['insight']}/{total_insight} insight puzzles.")
    print(f"AI solved{ai_scores['logic']}/{total_logic} logic puzzles")
    print(f"AI solved{ai_scores['insight']}/{total_insight} insight puzzles")

if __name__=="__main__":
   main()
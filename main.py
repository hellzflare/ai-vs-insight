def main():
    print("Welcome to AI Limits simulator")
    human_scores={"logic":0,"insight":0}
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

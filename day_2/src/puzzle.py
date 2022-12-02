import pandas as pd

score_type = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

strat_result = {
    "Z": 6,
    "Y": 3,
    "X": 0
}


def calc_score(input_list):
    score = 0
    for game in input_list:
        player_1 = game[:1]
        player_2 = game [-1]
        matrix = pd.DataFrame(
            [
                [3, 6, 0],
                [0, 3, 6],
                [6, 0, 3]
            ], columns=["X", "Y", "Z"], index=["A", "B", "C"]
        )
        game_score = matrix.loc[player_1][player_2]
        choice = score_type[player_2]
        score += game_score + choice
    return score

def calc_strat(input_list):
    score = 0
    for game in input_list:
        player_1 = game[:1]
        strat = game[-1]
        matrix = pd.DataFrame(
            [
                [3, 6, 0],
                [0, 3, 6],
                [6, 0, 3]
            ], columns=["X", "Y", "Z"], index=["A", "B", "C"]
        )
        score_list = matrix.loc[player_1]
        for i, x in enumerate(score_list):
            if x == strat_result[strat]:
                score += i + 1 + strat_result[strat]
    return score



with open("day_2/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]

    print(f"The score for round 1 were: {calc_score(list_input)}")
    print(f"The score for the super secret strategy was: {calc_strat(list_input)}")

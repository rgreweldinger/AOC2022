from src.puzzle import calc_puzzle_1, calc_puzzle_2


def test_calc_score():
    with open("day_5/tests/test_input.txt", "r") as input:
        columns, moves = input.read().split("\n\n")
        moves = moves.split("\n")
        column_size = 3
        result = calc_puzzle_1(columns, moves, column_size)
    assert result == "CMZ"


def test_calc_strat():
    with open("day_5/tests/test_input.txt", "r") as input:
        columns, moves = input.read().split("\n\n")
        moves = moves.split("\n")
        column_size = 3
        result = calc_puzzle_2(columns, moves, column_size)
    assert result == "MCD"

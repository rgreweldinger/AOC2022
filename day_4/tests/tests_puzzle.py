from src.puzzle import calc_puzzle_1, calc_puzzle_2


def test_calc_score():
    with open("day_4/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        result = calc_puzzle_1(list_input)
    assert result == 2


def test_calc_strat():
    with open("day_4/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        result = calc_puzzle_2(list_input)
    assert result == 4

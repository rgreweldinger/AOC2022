from src.puzzle import calc_score, calc_strat


def test_calc_score():
    with open("day_2/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        result = calc_score(list_input)
    assert result == 15


def test_calc_strat():
    with open("day_2/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        result = calc_strat(list_input)
    assert result == 12

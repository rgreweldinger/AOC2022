from src.puzzle import calc_puzzle_1, calc_puzzle_2


def test_calc_1():
    with open("day_7/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        output = calc_puzzle_1(list_input)
    assert output == 95437


def test_calc_2():
    with open("day_7/tests/test_input.txt", "r") as input:
        list_input = [cookie.strip() for cookie in input]
        output = calc_puzzle_2(list_input)
    assert output == 24933642

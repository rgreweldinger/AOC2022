from src.puzzle import calc_puzzle_1, calc_puzzle_2


def test_calc_1():
    with open("day_9/tests/test_input.txt", "r") as input:
        test_1, test_2 = input.read().split("\n\n")
        list_input = test_1.split("\n")
        print(list_input)
        output = calc_puzzle_1(list_input)
    assert output == 12


def test_calc_2():
    with open("day_9/tests/test_input.txt", "r") as input:
        test_1, test_2 = input.read().split("\n\n")
        list_input = test_2.split("\n")
        print(list_input)
        output = calc_puzzle_2(list_input)
    assert output == 36

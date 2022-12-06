from src.puzzle import calc_puzzle


def test_calc():
    with open("day_6/tests/test_input.txt", "r") as input:
        input_string = input.readline()
        output = calc_puzzle(input_string, 4)
    assert output == 7

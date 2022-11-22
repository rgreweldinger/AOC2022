from src.puzzle import calc_elfs, calc_max_elf, calc_top_range_elf


test_dict = {"elf_1": 7, "elf_2": 11, "elf_3": 24}

def test_calc_elf():
    with open("/Users/r.greweldinger/workspace/AOC2022/day_1/tests/test_input.txt", "r") as input:
        cookie_dict = calc_elfs(input)
        assert cookie_dict == test_dict


def test_calc_max_elf(test_dict=test_dict):
    max_elf, max_elf_value = calc_max_elf(test_dict)
    assert max_elf == "elf_3", max_elf_value == 24


def test_calc_top_three_elf(test_dict=test_dict):
    top_three_elf_value = calc_top_range_elf(3, test_dict)
    assert top_three_elf_value == 42

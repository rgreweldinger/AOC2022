import pytest


def calc_elfs(input_file):
    list_input = [cookie.strip() for cookie in input_file]
            
    elf_counter = 1
    cookie_dict = {}
    elf = "elf_" + str(elf_counter)

    for cookie in list_input:
        if cookie == "":
            elf_counter += 1
            elf = "elf_" + str(elf_counter)

        try:
            cookie_dict.update({elf: cookie_dict[elf] + int(cookie)})
        except KeyError:
            cookie_dict.update({elf: int(cookie) if cookie != "" else 0})

    return cookie_dict


def calc_max_elf(cookie_dict):
    max_elf = max(cookie_dict, key=cookie_dict.get)
    max_elf_value = cookie_dict[max_elf]
    return max_elf, max_elf_value


def calc_top_range_elf(top_range, cookie_dict):
    value = 0

    for x in range(top_range):
        max_elf, max_elf_value = calc_max_elf(cookie_dict)
        value += max_elf_value
        cookie_dict.pop(max_elf)
    
    return value


with open("/Users/r.greweldinger/workspace/AOC2022/day_1/src/input.txt", "r") as input:
    cookie_dict = calc_elfs(input)

max_elf, max_elf_value = calc_max_elf(cookie_dict)
print(f"The elf with the highest value is {max_elf} with {max_elf_value} calories")

top_three_elfs_value = calc_top_range_elf(3, cookie_dict)
print(f"The top 3 elfs together hold a calorie value of {top_three_elfs_value} worth in cookies")

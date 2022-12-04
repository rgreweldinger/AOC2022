dict_lower = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r" :18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

dict_upper = {}
for key, value in dict_lower.items():
    dict_upper.update({key.upper(): value + 26})


def calc_puzzle_1(list_input):
    bag_value_total = 0
    for bag in list_input:
        c1 = bag[int(len(bag)/2):]
        c2 = bag[:int(-len(bag)/2)]
        dupe_check = []
        for item in c1:
            if item in list(c2) and item not in dupe_check:
                dupe_check.append(item)
                bag_value = dict_lower[item] if item.islower() == True else dict_upper[item]
                bag_value_total += bag_value
    return bag_value_total


def calc_puzzle_2(list_input):
    bag_value_total = 0
    for i in range(0, len(list_input), 3):
        group = list(list_input[i:i + 3])
        dupe_check = []
        for item in group[0]:
            if item in list(group[1]) and item in list(group[2]) and item not in dupe_check:
                dupe_check.append(item)
                bag_value = dict_lower[item] if item.islower() == True else dict_upper[item]
                bag_value_total += bag_value
    return bag_value_total


with open("day_3/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    print(calc_puzzle_1(list_input))
    print(calc_puzzle_2(list_input))


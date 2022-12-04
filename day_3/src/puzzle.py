def calc_puzzle_1(list_input):
    bag_value_total = 0
    for bag in list_input:
        c1 = bag[int(len(bag)/2):]
        c2 = bag[:int(-len(bag)/2)]
        dupe_check = []
        for item in c1:
            if item in list(c2) and item not in dupe_check:
                dupe_check.append(item)
                bag_value = (ord(item) - 96) if item.islower() == True else (ord(item) - 38)
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
                bag_value = (ord(item) - 96) if item.islower() == True else (ord(item) - 38)
                bag_value_total += bag_value
    return bag_value_total


with open("day_3/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    print(calc_puzzle_1(list_input))
    print(calc_puzzle_2(list_input))

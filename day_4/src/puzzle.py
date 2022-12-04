def calc_puzzle_1(list_input):
    count = 0
    for line in list_input:
        sections = line.split(",")
        sections_1 = range(int(sections[0].split("-")[0]), int(sections[0].split("-")[-1]) + 1)
        sections_2 = range(int(sections[1].split("-")[0]), int(sections[1].split("-")[-1]) + 1)
        if sections_1[0] <= sections_2[0] and sections_1[-1] >= sections_2 [-1]:
            count += 1
        elif sections_1[0] >= sections_2[0] and sections_1[-1] <= sections_2 [-1]:
            count += 1
    return count


def calc_puzzle_2(list_input):
    count = 0
    for line in list_input:
        sections = line.split(",")
        sections_1 = range(int(sections[0].split("-")[0]), int(sections[0].split("-")[-1]) + 1)
        sections_2 = range(int(sections[1].split("-")[0]), int(sections[1].split("-")[-1]) + 1)
        if sections_1[0] >= sections_2[0] and sections_1[0] <= sections_2[-1]:
            for x in sections_1:
                if x >= sections_2[0] and x <= sections_2[-1]:
                    count += 1
                    break
        elif sections_2[0] >= sections_1[0] and sections_2[0] <= sections_1[-1]:
            for x in sections_2:
                if x >= sections_1[0] and x <= sections_1[-1]:
                    count += 1
                    break
    return count

with open("day_4/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    calc_puzzle_1(list_input)
    calc_puzzle_2(list_input)

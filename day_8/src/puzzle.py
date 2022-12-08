def calc_puzzle_1(trees):
    solution = 0
    for j, row in enumerate(trees):
        for i, tree in enumerate(row):
            left = row[:i]
            left_visible = all(int(x) < int(tree) for x in left)

            right = row [:i:-1]
            right_visible = all(int(x) < int(tree) for x in right)

            column = [y[i] for y in trees]
            top = column[:j]
            top_visible = all(int(x) < int(tree) for x in top)

            bottom = column[:j:-1]
            bottom_visible = all(int(x) < int(tree) for x in bottom)

            if left_visible or right_visible or top_visible or bottom_visible:
                solution += 1

    return solution


def calc_puzzle_2(trees):
    scenics = []
    for j, row in enumerate(trees):
        for i, tree in enumerate(row):
            left = row[:i]
            left_perspective = left[::-1]
            count_left = 0
            for c in left_perspective:
                if len(left_perspective) == 0:
                    break
                count_left += 1
                if int(tree) <= int(c):
                    break
            right = row[:i:-1]
            right_perspective = right[::-1]
            count_right = 0
            for c in right_perspective:
                if len(right_perspective) == 0:
                    break
                count_right += 1
                if int(tree) <= int(c):
                    break
            column = [y[i] for y in trees]
            top = column[:j]
            top_perspective = top[::-1]
            count_top = 0
            for c in top_perspective:
                if len(top_perspective) == 0:
                    break
                count_top += 1
                if int(tree) <= int(c):
                    break
            bottom = column[:j:-1]
            bottom_perspective = bottom[::-1]
            count_bottom = 0
            for c in bottom_perspective:
                if len(bottom_perspective) == 0:
                    break
                count_bottom += 1
                if int(tree) <= int(c):
                    break
            scenics.append(count_left*count_right*count_top*count_bottom)
    solution = max(scenics)
    return solution


with open("day_8/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    print(calc_puzzle_1(list_input))
    print(calc_puzzle_2(list_input))

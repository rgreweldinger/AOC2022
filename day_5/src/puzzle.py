import regex as re


def calc_puzzle_1(columns, moves, column_size):
    end_columns = [[] for i in range(column_size + 1)]  # add extra column for 0 index

    for row in columns.split("\n")[-2::-1]:  # remove numbers row and flip upside down
        for x, column in enumerate(row[1::4]):
            if column != " ":
                end_columns[x + 1].append(column)

    end_moves = []
    for move in moves:
        move_x = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(1)
        move_from = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(2)
        move_to = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(3)
        end_moves.append([move_x, move_from, move_to])

    for move_x, move_from, move_to in end_moves:
        for x in range(int(move_x)):
            end_columns[int(move_to)].append(end_columns[int(move_from)].pop())

    calc_1 = [column[-1] for column in end_columns[1:]]
    result_1 = "".join(calc_1)
    return result_1


def calc_puzzle_2(columns, moves, column_size):
    end_columns_2 = [[] for i in range(column_size + 1)]  # add extra column for 0 index

    for row in columns.split("\n")[-2::-1]:  # remove numbers row and flip upside down
        for x, column in enumerate(row[1::4]):
            if column != " ":
                end_columns_2[x + 1].append(column)

    end_moves = []
    for move in moves:
        move_x = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(1)
        move_from = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(2)
        move_to = re.search(r"move (\d*) from (\d*) to (\d*)", move).group(3)
        end_moves.append([move_x, move_from, move_to])

    for move_x, move_from, move_to in end_moves:
        end_columns_2[int(move_to)].extend(end_columns_2[int(move_from)][-int(move_x):])
        del end_columns_2[int(move_from)][-int(move_x):]

    calc_2 = [column[-1] for column in end_columns_2[1:]]
    result_2 = "".join(calc_2)
    return result_2


with open("day_5/src/input.txt", "r") as input:
    columns, moves = input.read().split("\n\n")
    moves = moves.split("\n")
    column_size = 9
    print(calc_puzzle_1(columns, moves, column_size))
    print(calc_puzzle_2(columns, moves, column_size))

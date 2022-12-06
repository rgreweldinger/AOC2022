def calc_puzzle(input_string, batch):
    for count, char in enumerate(range(batch, len(input_string))):
        unique_set = set(input_string[char-batch:char])
        if len(unique_set) == batch:
            return count+batch


with open("day_6/src/input.txt", "r") as input:
    input_string = input.readline()
    print(calc_puzzle(input_string, 4))
    print(calc_puzzle(input_string, 14))

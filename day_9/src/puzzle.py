def calc_puzzle_1(list_input):
    visited = set()
    h_x = 0
    h_y = 0
    t_x = 0
    t_y = 0
    for line in list_input:
        dir = line.split(" ")[0]
        mag = int(line.split(" ")[1])
        if dir == "R":
            for _ in range(mag):
                h_x += 1
                movement = [h_x - t_x, h_y - t_y]
                if movement[0] > 1:
                    t_x += 1
                    t_y = h_y
                    visited.add(str(t_x)+"|"+str(t_y))                
        if dir == "L":
            for _ in range(mag):
                h_x -= 1
                movement = [h_x - t_x, h_y - t_y]
                if movement[0] < -1:
                    t_x -= 1
                    t_y = h_y
                    visited.add(str(t_x)+"|"+str(t_y))                
        if dir == "U":
            for _ in range(mag):
                h_y += 1
                movement = [h_x - t_x, h_y - t_y]
                if movement[1] > 1:
                    t_y += 1
                    t_x = h_x
                    visited.add(str(t_x)+"|"+str(t_y))                
        if dir == "D":
            for _ in range(mag):
                h_y -= 1
                movement = [h_x - t_x, h_y - t_y]
                if movement[1] < -1:
                    t_y -= 1
                    t_x = h_x
                    visited.add(str(t_x)+"|"+str(t_y))
    return len(visited)       


def calc_puzzle_2(list_input):
    visited = set()
    positions = {
        "0_x": 0,
        "0_y": 0,
    }
    for i in range(1, 10):
        positions.update({
            f"{i}_x": 0,
            f"{i}_y": 0,
        })
    for line in list_input:
        dir = line.split(" ")[0]
        mag = int(line.split(" ")[1])
        for _ in range(mag):
            if dir == "R":
                positions["0_x"] += 1
            if dir == "L":
                positions["0_x"] -= 1
            if dir == "U":
                positions["0_y"] += 1
            if dir == "D":
                positions["0_y"] -= 1
            for i in range(1, 10):
                movement = [positions[f"{i-1}_x"] - positions[f"{i}_x"], positions[f"{i-1}_y"] - positions[f"{i}_y"]]
                if movement[0] > 1:
                    positions[f"{i}_x"] += 1
                    positions[f"{i}_y"] += 1 if movement[1] > 0 else -1 if movement[1] < 0 else 0
                elif movement[0] < -1:
                    positions[f"{i}_x"] -= 1
                    positions[f"{i}_y"] += 1 if movement[1] > 0 else -1 if movement[1] < 0 else 0
                elif movement[1] > 1:
                    positions[f"{i}_y"] += 1
                    positions[f"{i}_x"] += 1 if movement[0] > 0 else -1 if movement[0] < 0 else 0
                elif movement[1] < -1:
                    positions[f"{i}_y"] -= 1
                    positions[f"{i}_x"] += 1 if movement[0] > 0 else -1 if movement[0] < 0 else 0
                visited.add(str(positions["9_x"])+"|"+str(positions["9_y"]))
    return len(visited)


with open("day_9/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    print(calc_puzzle_1(list_input))
    print(calc_puzzle_2(list_input))

def calc_puzzle_1(list_input):    
    size_per_file = {}
    size_per_directory = {}
    list_directories = []

    for line in list_input:        
        if line == '$ cd ..':
            current_path = current_path.rsplit("/", 1)[0]
        elif line == '$ cd /':
            current_path = "/"
        elif line.startswith('$ cd '):
            if current_path == "/":
                current_path += line.split(" ")[-1]
            else:
                current_path += "/" + line.split(" ")[-1]      
        elif line.startswith('dir'):
            list_line = line.split(" ")
            if current_path == "/":
                list_directories.append(current_path + list_line[1])             
            else:
                list_directories.append(current_path + "/" + list_line[1])             
        elif line[0].isdigit():
            list_line = line.split(" ")
            size_per_file[current_path + list_line[1]] = int(list_line[0])

    for directory in list_directories:
        directory_size = 0
        for file, file_size in size_per_file.items():
            if file.startswith(directory):
                directory_size += file_size
        size_per_directory.update({directory: directory_size})
        
    solution = 0
    for k, v in size_per_directory.items():
        if v < 100000:
            solution += v

    return solution


def calc_puzzle_2(input_string):
    size_per_file = {}
    size_per_directory = {}
    list_directories = []

    for line in input_string:        
        if line == '$ cd ..':
            current_path = current_path.rsplit("/", 1)[0]
        elif line == '$ cd /':
            current_path = "/"
        elif line.startswith('$ cd '):
            if current_path == "/":
                current_path += line.split(" ")[-1]
            else:
                current_path += "/" + line.split(" ")[-1]      
        elif line.startswith('dir'):
            list_line = line.split(" ")
            if current_path == "/":
                list_directories.append(current_path + list_line[1])             
            else:
                list_directories.append(current_path + "/" + list_line[1])             
        elif line[0].isdigit():
            list_line = line.split(" ")
            size_per_file[current_path + list_line[1]] = int(list_line[0])

    for directory in list_directories:
        directory_size = 0
        for file, file_size in size_per_file.items():
            if file.startswith(directory):
                directory_size += file_size
        size_per_directory.update({directory: directory_size})
    
    total_memory_in_use = sum(size_per_file.values())
    list_of_possibilities = []
    for k, v in size_per_directory.items():
        if total_memory_in_use - v < 40000000:
            list_of_possibilities.append(v)
    
    solution = min(list_of_possibilities)
    return solution


with open("day_7/src/input.txt", "r") as input:
    list_input = [cookie.strip() for cookie in input]
    print(calc_puzzle_1(list_input))
    print(calc_puzzle_2(list_input))

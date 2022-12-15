import re
import time

def create_not_open_list(file_path):
    file = open(file_path)
    lines = [line for line in re.split("\n", file.read()) if line != ""]
    file.close()

    rock_paths = []
    max_y = 0
    for line in lines:
        coords = [list(t) for t in re.findall("([0-9]+),([0-9]+)", line)]
        for i in range(len(coords)):
            coords[i][0], coords[i][1] = int(coords[i][0]), int(coords[i][1])
            if coords[i][1] > max_y: max_y = coords[i][1]
        rock_paths.append(coords)

    not_open = []
    for rock_path in rock_paths:
        for i in range(len(rock_path) - 1):
            x1, x2, y1, y2 = rock_path[i][0], rock_path[i+1][0], rock_path[i][1], rock_path[i+1][1]
            if x1 == x2:  
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if (x1, y) not in not_open: not_open.append((x1, y))
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if (x, y1) not in not_open: not_open.append((x, y1))
    return [not_open, max_y]
        
def is_open_spot(coords, not_open, max_y):
    if (coords[0], coords[1]) in not_open: return False
    elif coords[1] > max_y + 1: return False
    else: return True

def find_next_open_spot(source, not_open, max_y, floor):
    if not is_open_spot(source, not_open, max_y): return source
    else:
        if not floor:
            if source[1] + 1 > max_y: return "void"
        if is_open_spot((source[0], source[1] + 1), not_open, max_y): return find_next_open_spot((source[0], source[1] + 1), not_open, max_y, floor)
        elif is_open_spot((source[0] - 1, source[1] + 1), not_open, max_y): return find_next_open_spot((source[0] - 1, source[1] + 1), not_open, max_y, floor)
        elif is_open_spot((source[0] + 1, source[1] + 1), not_open, max_y): return find_next_open_spot((source[0] + 1, source[1] + 1), not_open, max_y, floor)
        else: return source

def drop_sand(source, not_open, max_y, floor, n_sand):
    while True:
        next_open_spot = find_next_open_spot(source, not_open, max_y, floor)
        if floor:
            if next_open_spot == source:
                n_sand += 1
                not_open.append(source)
                break
        else:
            if next_open_spot == "void": break
        not_open.append(next_open_spot)
        n_sand += 1
    return n_sand

file_path = "Day14Input.txt"
not_open_info = create_not_open_list(file_path)
not_open, max_y = not_open_info[0], not_open_info[1]

source = (500, 0)
n_sand_0 = 0
n_sand_1 = drop_sand(source, not_open, max_y, False, n_sand_0)
n_sand_2 = drop_sand(source, not_open, max_y, True, n_sand_0)

# puzzle answers
print("puzzle 1 answer =", n_sand_1)
print("puzzle 2 answer =", n_sand_1 + n_sand_2)

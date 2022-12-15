import re

file = open("Day14Input.txt")
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
n_rocks = len(not_open)
    
def open_spot(coords, not_open):
    if (coords[0], coords[1]) in not_open: return False
    elif coords[1] > max_y + 1: return False
    else: return True

def find_next_open_spot(source, not_open, floor):
    if not open_spot(source, not_open): return source
    else:
        if not floor:
            if source[1] + 1 > max_y: return "void"
        if open_spot((source[0], source[1] + 1), not_open): return find_next_open_spot((source[0], source[1] + 1), not_open, floor)
        elif open_spot((source[0] - 1, source[1] + 1), not_open): return find_next_open_spot((source[0] - 1, source[1] + 1), not_open, floor)
        elif open_spot((source[0] + 1, source[1] + 1), not_open): return find_next_open_spot((source[0] + 1, source[1] + 1), not_open, floor)
        else: return source

def drop_sand(source, not_open, floor):
    while True:
        next_open_spot = find_next_open_spot(source, not_open, floor)
        if floor:
            if next_open_spot == source:
                not_open.append(source)
                break
        else:
            if next_open_spot == "void": break
        not_open.append(next_open_spot)
    return len(not_open) - n_rocks

# puzzle answers
print("puzzle 1 answer =", drop_sand((500,0), not_open, False))
print("puzzle 2 answer =", drop_sand((500,0), not_open, True))

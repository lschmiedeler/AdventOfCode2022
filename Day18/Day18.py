import re

def find_sa(file_path):
    file = open(file_path)
    lines = file.readlines()
    file.close()
    
    cubes = []
    sa = 0
    for line in lines:
        cube = re.findall("([0-9]*),([0-9]*),([0-9]*)", line)[0]
        x, y, z = int(cube[0]), int(cube[1]), int(cube[2])
        new_sa = 6
        if (x + 1, y, z) in cubes: new_sa -= 2
        if (x - 1, y, z) in cubes: new_sa -= 2
        if (x, y + 1, z) in cubes: new_sa -= 2
        if (x, y - 1, z) in cubes: new_sa -= 2
        if (x, y, z + 1) in cubes: new_sa -= 2
        if (x, y, z - 1) in cubes: new_sa -= 2
        sa += new_sa
        cubes.append((x, y, z))
    return [cubes, sa]

# puzzle answers
print("puzzle 1 answer =", find_sa("Day18Input.txt")[1])

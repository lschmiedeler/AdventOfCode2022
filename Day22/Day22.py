import re
import numpy as np

class TracePath:
    def __init__(self):
        file = open("Day22Input.txt")
        lines = file.readlines()
        max_line_len = max([len(line) - 1 for line in lines])
        board_map = []
        path_next = False
        for line in lines:
            if line == "\n": path_next = True
            elif path_next: 
                self.path_numbers = re.split("[R|L]", line)
                self.path_letters = re.findall("[R|L]", line)
            else:
                line_list = list(line[:-1])
                if len(line_list) < max_line_len:
                    for i in range(max_line_len - len(line_list)): line_list.append(" ")
                board_map.append(line_list)
        file.close()
        self.board_map = np.array(board_map)
        self.position = [0, 0]
        self.facing = "R"
    
    def set_starting_position(self):
        for i in range(self.board_map.shape[1]):
            if self.board_map[0, i] == ".":
                self.position = [0, i]
                break
            
    def update_position(self, n_tiles):
        for i in range(1, n_tiles + 1):
            if self.facing == "R": 
                new = self.position[1] + 1
                if new >= self.board_map.shape[1]: tile = ""
                else: tile = self.board_map[self.position[0], new].strip()
                if tile == "":
                    wrap = False
                    i = 0
                    while not wrap and i < self.board_map.shape[1]:
                        temp_tile = self.board_map[self.position[0], i]
                        if temp_tile in [".", "#"]:
                            wrap = True
                            new = i
                            tile = temp_tile
                        i += 1
            elif self.facing == "D": 
                new = self.position[0] + 1
                if new >= self.board_map.shape[0]: tile = ""
                else: tile = self.board_map[new, self.position[1]].strip()
                if tile == "": 
                    wrap = False
                    i = 0
                    while not wrap and i < self.board_map.shape[0]:
                        temp_tile = self.board_map[i, self.position[1]]
                        if temp_tile in [".", "#"]:
                            wrap = True
                            new = i
                            tile = temp_tile
                        i += 1
            elif self.facing == "L":
                new = self.position[1] - 1
                if new < 0: tile = ""
                else: tile = self.board_map[self.position[0], new].strip()
                if tile == "":
                    wrap = False
                    i = self.board_map.shape[1] - 1
                    while not wrap and i >= 0:
                        temp_tile = self.board_map[self.position[0], i]
                        if temp_tile in [".", "#"]:
                            wrap = True
                            new = i
                            tile = temp_tile
                        i -= 1
            elif self.facing == "U":
                new = self.position[0] - 1
                if new < 0: tile = ""
                else: tile = self.board_map[new, self.position[1]].strip()
                if tile == "": 
                    wrap = False
                    i = self.board_map.shape[0] - 1
                    while not wrap and i >= 0:
                        temp_tile = self.board_map[i, self.position[1]]
                        if temp_tile in [".", "#"]:
                            wrap = True
                            new = i
                            tile = temp_tile
                        i -= 1
            if tile == "#": break
            if self.facing in ["R", "L"]: self.position[1] = new
            else: self.position[0] = new
            
    def update_facing(self, rotation):
        if rotation == "R":
            if self.facing == "R": self.facing = "D"
            elif self.facing == "D": self.facing = "L"
            elif self.facing == "L": self.facing = "U"
            elif self.facing == "U": self.facing = "R"
        elif rotation == "L":
            if self.facing == "R": self.facing = "U"
            elif self.facing == "U": self.facing = "L"
            elif self.facing == "L": self.facing = "D"
            elif self.facing == "D": self.facing = "R"
        
tp = TracePath()
tp.set_starting_position()
for i in range(len(tp.path_numbers)):
    tp.update_position(int(tp.path_numbers[i]))
    if i < len(tp.path_numbers) - 1: tp.update_facing(tp.path_letters[i])
    
if tp.facing == "R": final_facing = 0
elif tp.facing == "D": final_facing = 1
elif tp.facing == "L": final_facing = 2
elif tp.facing == "U": final_facing = 3

# puzzle answers
print("puzzle 1 answer =", 1000 * (tp.position[0] + 1) + 4 * (tp.position[1] + 1) + final_facing)
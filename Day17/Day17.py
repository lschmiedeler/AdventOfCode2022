class RockFall:
    def __init__(self):
        file_path = "Day17Input.txt"
        file = open(file_path)
        self.jets = list(file.readlines()[0].strip())
        file.close()
        
        self.rocks = [[] for i in range(7)]
        self.max_ys = [1 for i in range(7)]
        self.max_y = max(self.max_ys)
        self.rock_type = 1
        self.jets_i = 0
        self.jet = self.jets[self.jets_i]
    
    def get_min_x(self, rock):
        return min([x for (x, y) in rock])
        
    def get_max_x(self, rock):
        return max([x for (x, y) in rock])
    
    def update_rock_type(self):
        if self.rock_type == 5: self.rock_type = 1
        else: self.rock_type += 1
        
    def update_jet(self):
        self.jet = self.jets[self.jets_i]
        if self.jets_i == len(self.jets) - 1: self.jets_i = 0
        else: self.jets_i += 1
            
    def update_rocks(self, rock):
        for i in range(len(self.rocks)):
            self.rocks[i] += [y for (x, y) in rock if x == i + 1]
            self.rocks[i] = list(set(self.rocks[i]))
        self.max_ys = [max(rock_col) + 1 if len(rock_col) > 0 else 1 for rock_col in self.rocks]
        self.max_y = max(self.max_ys)

    def get_rock_start_pos(self):
        if self.rock_type == 1: return [(x, 3 + self.max_y) for x in range(3, 7)]
        elif self.rock_type == 2: return [(4, 3 + self.max_y + y) for y in range(3)] + [(3, 4 + self.max_y), (5, 4 + self.max_y)]
        elif self.rock_type == 3: return [(x, 3 + self.max_y) for x in range(3, 6)] + [(5, 4 + self.max_y + y) for y in range(2)]
        elif self.rock_type == 4: return [(3, 3 + self.max_y + y) for y in range(4)]
        else: return [(x, 3 + self.max_y) for x in range(3, 5)] + [(x, 4 + self.max_y) for x in range(3, 5)]  
    
    def check_collision(self, rock, fall = False):
        if not fall:
            if self.jet == ">": new_rock = [(x + 1, y) for (x, y) in rock]
            else: new_rock = [(x - 1, y) for (x, y) in rock]
        else:
            new_rock = [(x, y - 1) for (x, y) in rock]
        for i in range(len(self.rocks)):
            for y in [y for (x, y) in new_rock if x == i + 1]:
                if fall and y == 0: return True
                if y in self.rocks[i]: return True
        return False
    
    def drop_rock(self, sleep = False):
        rock = self.get_rock_start_pos()
        bottom = False
        while not bottom:
            self.update_jet()
            if not self.check_collision(rock):
                if self.jet == ">": 
                    if self.get_max_x(rock) < len(self.rocks): rock = [(x + 1, y) for (x, y) in rock]
                else:
                    if self.get_min_x(rock) > 1: rock = [(x - 1, y) for (x, y) in rock]
            bottom = self.check_collision(rock, fall = True)
            if not bottom: rock = [(x, y - 1) for (x, y) in rock]
        self.update_rocks(rock)
        self.update_rock_type()
        return self.max_y - 1
        
rf = RockFall()
for i in range(2022): rf.drop_rock()

# puzzle answers
print("puzzle 1 answer =", rf.max_y - 1)

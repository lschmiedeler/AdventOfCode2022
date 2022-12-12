import re

class KeepAway:
    def __init__(self):
        file = open("Day11Input.txt")
        lines = file.read()
        file.close()
        
        self.monkeys = [list(t) for t in re.findall("\s*Starting items: (.*)\s*Operation: new = (.*)\s*Test: divisible by (.*)\s*If true: throw to monkey (.*)\s*If false: throw to monkey (.*)\s*", lines)]
        tests = []
        for i in range(len(self.monkeys)):
            self.monkeys[i][0] = [int(x) for x in re.split(", ", self.monkeys[i][0])]
            self.monkeys[i][2], self.monkeys[i][3], self.monkeys[i][4] = int(self.monkeys[i][2]), int(self.monkeys[i][3]), int(self.monkeys[i][4])
            tests.append(self.monkeys[i][2])
        
        self.magic_number = 1
        for test in tests: self.magic_number *= test
    
    def play_rounds(self, n_rounds, divide_by_3):
        inspections = [0] * len(self.monkeys)
        for i in range(n_rounds):
            for j in range(len(self.monkeys)):
                monkey = self.monkeys[j]
                for old in monkey[0]:
                    inspections[j] += 1
                    worry_level = eval(monkey[1])
                    if divide_by_3: worry_level = int(worry_level / 3)
                    worry_level = int(worry_level % self.magic_number)
                    if (worry_level % monkey[2] == 0): self.monkeys[monkey[3]][0].append(worry_level)
                    else: self.monkeys[monkey[4]][0].append(worry_level)
                    monkey[0] = monkey[0][1:]
        return sorted(inspections)[-2] * sorted(inspections)[-1]

KeepAway1 = KeepAway()
KeepAway2 = KeepAway()

# puzzle answers
print("puzzle 1 answer =", KeepAway1.play_rounds(20, True))
print("puzzle 2 answer =", KeepAway2.play_rounds(10000, False))

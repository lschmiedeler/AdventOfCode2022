import re

class Monkey:
    def __init__(self, monkey_info):
        self.items = [int(x) for x in re.split(", ", monkey_info[0])]
        self.operation = monkey_info[1]
        self.test, self.if_true, self.if_false = int(monkey_info[2]), int(monkey_info[3]), int(monkey_info[4])
        self.inspections = 0
    
    def __inspect_item(self, modulo, divide_by_3):
        self.inspections += 1
        old = self.items[0]
        self.items[0] = int(eval(self.operation) % modulo)
        if divide_by_3: self.items[0] = int(self.items[0] / 3)
        
    def throw_item(self, modulo, divide_by_3):
        self.__inspect_item(modulo, divide_by_3)
        thrown_item = self.items[0]
        self.items = self.items[1:]
        return thrown_item
    
    def catch_item(self, item):
        self.items.append(item)
    
    def test_item(self, item):
        if item % self.test ==  0: return True
        else: return False
        
class KeepAway:
    def __init__(self, all_monkey_info):
        self.monkeys = []
        all_monkey_info = [monkey_info for monkey_info in re.split("\n\n", all_monkey_info) if monkey_info != ""]
        for monkey_info in all_monkey_info: self.monkeys.append(Monkey([list(t) for t in re.findall("\s*Starting items: (.*)\s*Operation: new = (.*)\s*Test: divisible by (.*)\s*If true: throw to monkey (.*)\s*If false: throw to monkey (.*)\s*", monkey_info)][0]))
        self.inspections = [0] * len(self.monkeys)
        self.modulo = 1
        for monkey in self.monkeys:
            self.modulo *= monkey.test
    
    def __update_inspections(self):
        for i in range(len(self.monkeys)): self.inspections[i] += self.monkeys[i].inspections
    
    def play_rounds(self, n_rounds, divide_by_3):
        for i in range(n_rounds):
            for j in range(len(self.monkeys)):
                monkey = self.monkeys[j]
                for item in monkey.items:
                    thrown_item = monkey.throw_item(self.modulo, divide_by_3)
                    if monkey.test_item(thrown_item) == True: self.monkeys[monkey.if_true].items.append(thrown_item)
                    else: self.monkeys[monkey.if_false].items.append(thrown_item)
        self.__update_inspections()
    
    def calculate_monkey_business(self):
        return sorted(self.inspections)[-2] * sorted(self.inspections)[-1]
                        
file = open("Day11Input.txt")
lines = file.read()
file.close()

KeepAway1 = KeepAway(lines)
KeepAway1.play_rounds(20, True)

KeepAway2 = KeepAway(lines)
KeepAway2.play_rounds(10000, False)

# puzzle answers
print("puzzle 1 answer =", KeepAway1.calculate_monkey_business())
print("puzzle 2 answer =", KeepAway2.calculate_monkey_business())

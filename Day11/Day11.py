import re

def play_rounds(n_rounds, divide_by_3):
    file = open("Day11Input.txt")
    lines = file.readlines()
    file.close()

    monkey = []
    monkeys = []
    tests = []
    for line in lines:
        if len(re.findall("Starting items: ", line)) > 0:
            starting_items = re.split(", ", re.split("Starting items: ", line)[1])
            starting_items = [int(item) for item in starting_items]
            monkey.append(starting_items)
        if len(re.findall("Operation: ", line)) > 0:
            operation = re.split("Operation: new = ", line)[1].strip()
            monkey.append(operation)
        if len(re.findall("Test: ", line)) > 0:
            test = int(re.split("Test: divisible by ", line)[1])
            monkey.append(test)
            tests.append(test)
        if len(re.findall("\s*If true: ", line)) > 0:
            if_true = int(re.split("\s*If true: throw to monkey ", line)[1])
            monkey.append(if_true)
        if len(re.findall("\s*If false: ", line)) > 0:
            if_false = int(re.split("\s*If false: throw to monkey ", line)[1])
            monkey.append(if_false)
        if line == "\n":
            monkeys.append(monkey)
            monkey = []
            
    magic_number = 1
    for test in tests: magic_number *= test
    inspections = [0] * len(monkeys)
    for i in range(n_rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for old in monkey[0]:
                inspections[i] += 1
                worry_level = eval(monkey[1])
                if divide_by_3: worry_level = int(worry_level / 3)
                worry_level = int(worry_level % magic_number)
                if (worry_level % monkey[2] == 0): monkeys[monkey[3]][0].append(worry_level)
                else: monkeys[monkey[4]][0].append(worry_level)
                monkey[0] = monkey[0][1:]
                
    return sorted(inspections)[-2] * sorted(inspections)[-1]

# puzzle answers
print("puzzle 1 answer =", play_rounds(20, True))
print("puzzle 2 answer =", play_rounds(10000, False))

import re

file_path = "Day21Input.txt"
file = open(file_path)
monkeys = {}
for line in file.readlines(): monkeys[re.findall("([a-z]*):", line)[0]] = re.findall(": (.*)", line)[0]
file.close()

def find_operation(job): return re.findall(" ([\+|\-|\*|/]) ", job)[0]

def find_new_monkeys(job): return job.split(f" {find_operation(job)} ")
    
def find_number(monkey):
    if monkeys[monkey].isnumeric(): return int(monkeys[monkey])
    else: 
        new_monkeys = find_new_monkeys(monkeys[monkey])
        return int(eval(f"{find_number(new_monkeys[0])} {find_operation(monkeys[monkey])} {find_number(new_monkeys[1])}"))

# puzzle answers
print("puzzle 1 answer =", find_number("root"))

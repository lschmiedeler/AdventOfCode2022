import re
import ast

file = open("Day13Input.txt")
lines = file.read()
file.close()

packets_pairs = []
for packet_pair in re.findall("(\[.*\])\n(\[.*\])\n", lines): packets_pairs.append([ast.literal_eval(packet_pair[0]), ast.literal_eval(packet_pair[1])])

def check_packets(p):
    if type(p[0]) == int and type(p[1]) == int: # both integers
        if (p[0] < p[1]): return 1 # left side is smaller
        if (p[0] > p[1]): return 0 # right side is smaller
        else: return 2 # right and left sides are equal
    if type(p[0]) == list and type(p[1]) == list: # both lists
        if len(p[0]) == 0 and len(p[1]) > 0: return 1 # left side ran out of items
        for i in range(len(p[0])):
            if i > (len(p[1]) - 1): return 0 # right side ran out of items
            return_value = check_packets([p[0][i], p[1][i]])
            if i == len(p[0]) - 1 and len(p[1]) > i + 1 and return_value == 2: return 1 # left side ran out of items
            if return_value ==  0 or return_value == 1: return return_value
    else: # one integer and one list
        if type(p[0]) == list: return check_packets([p[0], [p[1]]])
        else: return check_packets([[p[0]], p[1]])

# https://i.stack.imgur.com/RwILJ.png
def merge(l, r):
    ordered_packets = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if check_packets([l[i], r[j]]) == 1: # left < right
            ordered_packets.append(l[i])
            i += 1
        else: # left >= right
            ordered_packets.append(r[j])
            j += 1
    ordered_packets += l[i:]
    ordered_packets += r[j:]
    return ordered_packets
def merge_sort(p):
    if len(p) == 0 or len(p) == 1: return p
    else:
        middle = len(p) // 2
        return merge(merge_sort(p[:middle]), merge_sort(p[middle:]))

right_order = []
for i in range(len(packets_pairs)):
    if check_packets(packets_pairs[i]) == 1: right_order.append(i + 1)

packets = []
for packet_pair in packets_pairs:
    packets.append(packet_pair[0])
    packets.append(packet_pair[1])
packets.append([[2]])
packets.append([[6]])
ordered_packets = merge_sort(packets)
    
# puzzle answers
print("puzzle 1 answer =", sum(right_order))
print("puzzle 2 answer =", (ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1))

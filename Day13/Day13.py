import re
import ast

class Packets:
    def __init__(self, file_path):
        file = open(file_path)
        lines = file.read()
        file.close()
        
        self.packets = [ast.literal_eval(packet) for packet in re.split("\n|\n\n", lines) if packet != ""]
    
    def __check_packets(self, p):
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
    def __merge(self, l, r):
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
    
    def __merge_sort(self, p):
        if len(p) == 0 or len(p) == 1: return p
        else:
            middle = int(len(p) / 2)
            return merge(merge_sort(p[:middle]), merge_sort(p[middle:]))
    
    def n_right_order(self):
        right_order = []
        for i in [2 * i for i in range(int(len(self.packets) / 2))]:
            if self.__check_packets([self.packets[i], self.packets[i + 1]]): right_order.append(int(i / 2) + 1)
        return sum(right_order)
    
    def order_packets(self, divider_1, divider_2):
        self.packets.append(divider_1)
        self.packets.append(divider_2)
        self.packets = self.__merge_sort(self.packets)
        return (ordered_packets.index(divider_1) + 1) * (ordered_packets.index(divider_2) + 1)
            
file_path = "Day13Input.txt"
AllPackets = Packets(file_path)
    
# puzzle answers
print("puzzle 1 answer =", AllPackets.n_right_order())
print("puzzle 2 answer =", AllPackets.order_packets([[2]], [[6]]))

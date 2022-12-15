import re
import networkx as nx # graph library

def create_heightmap_list(file_path):
    file = open(file_path)
    lines = file.read()
    file.close()

    lines_list = [line for line in re.split("\n", lines) if line != ""]
    nrow, ncol = len(lines_list), len(lines_list[0])
    
    return [re.sub("\s*", "", lines), nrow, ncol]

def create_nodes_list(heightmap):
    return list(range(len(heightmap)))
    
def create_edges_list(heightmap, nrow, ncol):
    edges = []
    for i in range(len(heightmap)):
        if (i % ncol != ncol - 1): # left
            if (ord(heightmap[i + 1]) <= ord(heightmap[i]) + 1): edges.append((i, i + 1))
        if (i % ncol != 0): # right
            if (ord(heightmap[i - 1]) <= ord(heightmap[i]) + 1): edges.append((i, i - 1))
        if (i > nrow - 1): # up
            if (ord(heightmap[i - ncol]) <= ord(heightmap[i]) + 1): edges.append((i, i - ncol))
        if (i < (nrow - 1) * ncol): # down
            if (ord(heightmap[i + ncol]) <= ord(heightmap[i]) + 1): edges.append((i, i + ncol))
    return edges

def find_starts_and_end(heightmap):
    start, end = re.search("S", heightmap).start(), re.search("E", heightmap).start()
    starts = [start]
    for i in range(len(heightmap)): 
        if heightmap[i] == "a": starts.append(i)
    return [re.sub("E", "z", re.sub("S", "a", heightmap)), starts, end]

file_path = "Day12Input.txt"
heightmap_info = create_heightmap_list(file_path)
heightmap, nrow, ncol = heightmap_info[0], heightmap_info[1], heightmap_info[2]

starts_and_end_info = find_starts_and_end(heightmap)
heightmap, starts, end = starts_and_end_info[0], starts_and_end_info[1], starts_and_end_info[2]
    
G = nx.DiGraph() # create a directed graph
G.add_nodes_from(create_nodes_list(heightmap)) # add the nodes
G.add_edges_from(create_edges_list(heightmap, nrow, ncol)) # add the edges

shortest_path = nx.shortest_path_length(G, starts[0], end)
min_shortest_path = shortest_path
for start in starts[1:]:
    if nx.has_path(G, start, end) == True:
        next_shortest_path = nx.shortest_path_length(G, start, end)
        if next_shortest_path < min_shortest_path:
            min_shortest_path = next_shortest_path

# puzzle answers
print("puzzle 1 answer =", shortest_path)
print("puzzle 2 answer =", min_shortest_path)

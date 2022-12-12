import re
import networkx as nx # graph library

file = open("Day12Input.txt")
lines = file.read()
file.close()

lines_list = [line for line in re.split("\n", lines) if line != ""]
ncol, nrow = len(lines_list[0]), len(lines_list)
heights = re.sub("\s*", "", lines)
start, end = re.search("S", heights).start(), re.search("E", heights).start()
other_starts = []
for i in range(len(heights)): 
    if heights[i] == "a": other_starts.append(i)
heights = re.sub("E", "z", re.sub("S", "a", heights))

nodes = list(range(len(heights)))
edges = []
for i in range(len(heights)):
    if (i % ncol != ncol - 1): # left
        if (ord(heights[i+1]) <= ord(heights[i]) + 1): edges.append((i, i+1))
    if (i % ncol != 0): # right
        if (ord(heights[i-1]) <= ord(heights[i]) + 1): edges.append((i, i-1))
    if (i > nrow - 1): # up
        if (ord(heights[i-ncol]) <= ord(heights[i]) + 1): edges.append((i, i-ncol))
    if (i < (nrow - 1) * ncol): # down
        if (ord(heights[i+ncol]) <= ord(heights[i]) + 1): edges.append((i, i+ncol))
        
G = nx.DiGraph() # create a directed graph
G.add_nodes_from(nodes) # add the nodes
G.add_edges_from(edges) # add the edges

shortest_path = nx.shortest_path_length(G, start, end)
min_shortest_path = nx.shortest_path_length(G, start, end)
for start in other_starts:
    if nx.has_path(G, start, end) == True:
        if nx.shortest_path_length(G, start, end) < min_shortest_path:
            min_shortest_path = nx.shortest_path_length(G, start, end)

# puzzle answers
print("puzzle 1 answer =", shortest_path)
print("puzzle 2 answer =", min_shortest_path)

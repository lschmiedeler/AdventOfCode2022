import re
import networkx as nx # graph library
from itertools import combinations
from collections import defaultdict

file_path = "Day16Input.txt"
file = open(file_path)
lines = file.readlines()
file.close()

G = nx.Graph()
for line in lines:
    line = re.findall("Valve ([A-Z]*) has flow rate=([0-9]*); tunnel(|s) lead(|s) to valve(|s) (.*)", line)[0]
    valve, flow_rate, to_valves = line[0], line[1], re.split(", ", line[5]) 
    G.add_node(valve, weight = int(flow_rate))
    for to_valve in to_valves: G.add_edge(valve, to_valve)
distances = dict(nx.all_pairs_shortest_path_length(G))

max_pressure_releases = defaultdict(dict)

def find_next_nodes(G, n, t):
    return [next_node for next_node in list(distances[n].keys()) if G.nodes[next_node]["weight"] > 0 and distances[n][next_node] + 1 < t]

def set_zero_graph_weights(G, nodes):
    G_new = G.copy()
    for node in nodes: G_new.nodes[node]["weight"] = 0
    return G_new

def find_new_time(G, node_0, node, t):
    return (t - distances[node_0][node] - 1)

def find_pressure_release(G, node_0, node, t):
    return G.nodes[node]["weight"] * find_new_time(G, node_0, node, t)

def find_max_pressure_release(G, n, t):
    next_nodes = find_next_nodes(G, n, t)
    next_nodes.sort()
    if len(next_nodes) == 0: return 0
    elif (n, t) in max_pressure_releases.keys() and str(next_nodes) in max_pressure_releases[(n, t)].keys(): return max_pressure_releases[(n, t)][str(next_nodes)]
    else:
        max_pressure_releases[(n, t)][str(next_nodes)] = max([find_pressure_release(G, n, nn, t) + find_max_pressure_release(set_zero_graph_weights(G, [nn]), nn, find_new_time(G, n, nn, t)) for nn in next_nodes])
        return max_pressure_releases[(n, t)][str(next_nodes)]

# puzzle answers
print("puzzle 1 answer =", find_max_pressure_release(G, "AA", 30))

import networkx as nx
import random

G = nx.Graph()

for node in range(1, 6):
    G.add_node(node)

while len(G.edges()) != 10:
    node1, node2 = random.sample(range(1, 6), 2)
    G.add_edge(node1, node2)

print(G.nodes())
print(G.edges())

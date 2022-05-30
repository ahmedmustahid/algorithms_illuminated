
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/scc/test_cases/testCase1.txt"
fileName = Path.home()/"work/sccTestCase.txt"
G = nx.DiGraph()

for line in open(fileName, "r"):
    k, v = map(int, line.split())
    if k != v:
        G.add_edge(k, v)
#G.add_edge(1, 2)
print(G.number_of_edges(2, 47647))
print(G.size())
print(G.number_of_nodes())
#nx.draw(G, with_labels = True)
##labels = nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
##labels = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
#plt.show()

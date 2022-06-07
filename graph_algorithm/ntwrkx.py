import pprint
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path
pp = pprint.PrettyPrinter(indent=4)
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/scc/test_cases/testCase1.txt"
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/testCases/test1.txt"
G = nx.DiGraph()

for line in open(fileName, "r"):
    k, v = map(int, line.split())
    if k != v:
        G.add_edge(k, v)
#G.add_edge(1, 2)
#print(G.number_of_edges(2, 47647))
print(G.size())
print(G.number_of_nodes())
print(fileName.parent)
print(fileName.stem)
print(f"scc {nx.number_strongly_connected_components(G)}")
pp.pprint([

    len(c)

    for c in sorted(

        nx.kosaraju_strongly_connected_components(G), key=len, reverse=True

    )

])
nx.draw(G, with_labels = True)
##labels = nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
##labels = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
plt.savefig(str(fileName.parent)+"/"+fileName.stem+".png")
#plt.show()

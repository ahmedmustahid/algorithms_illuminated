import collections
from pathlib import Path
import pprint
import sys
import networkx as nx
import matplotlib.pyplot as plt
from heap import Heap
#import more_itertools
pp = pprint.PrettyPrinter(width=41, compact=True)
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/dijkstraChallenge.txt"
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/testCase1.txt"

def createGraph(fileName):
    graph = collections.defaultdict(lambda : {'children': {}, 'length': 1000000})
    with open(fileName) as f:
        for line in f:
            test = line.split()
            #print(test)
            for child in test[1:]:
                node, weight = map(int, child.split(','))
                graph[int(test[0])]['children'][node] = weight
    #pp.pprint(graph)
    #sys.exit()
    return graph

def visualizeGraph(fileName):
    G = nx.DiGraph()
    graph = createGraph(fileName)

    for head in graph:
        for tail, weight in graph[head]['children'].items():
            G.add_edge(head, tail, weight = weight)
    print(G.size())
    print(G.number_of_nodes())
    pos = nx.spring_layout(G, seed=7)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, width=6)
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    #plt.show()
    imageName = str(fileName.parent) +"/" + fileName.stem + ".png"
    plt.savefig(imageName)
    print(f"{imageName} saved")

#visualizeGraph(fileName= fileName)

def dijkstraPathNetworkx(graph, tails):
    G = nx.DiGraph()
    #graph = createGraph(fileName)

    for head in graph:
        for tail, weight in graph[head]['children'].items():
            G.add_edge(head, tail, weight = weight)
    dijkstraLens = []
    for tail in tails:
        distance, _ = nx.single_source_dijkstra(G ,source=1, target= tail)
        dijkstraLens.append(distance)
    return dijkstraLens

if __name__ == "__main__":
    graph = createGraph(fileName)
    stack = [1]
    seenNodes = {1}
    edgeWeights = {}
    graph[stack[0]]['length'] = 0
    while stack:
        parent = stack.pop()
        for child, weight in graph[parent]['children'].items():
            if not child in seenNodes:
                edgeWeights[(parent, child)] = graph[parent]["length"] + weight
        if edgeWeights:
            minParent, minChild = min(edgeWeights, key= edgeWeights.get)
            #minWeight = min(edgeWeights.values())
            minWeight = edgeWeights[(minParent, minChild)]
            seenNodes.add(minChild)
            stack.append(minChild)
            edgeWeights.pop((minParent, minChild))
            
            graph[minChild]['length'] = min(minWeight, graph[minChild]['length'])
            #if minWeight < graph[minChild]['length']:
            #    graph[minChild]['length'] = minWeight


    #pp.pprint(graph)
    nodeMap = map(int, "7,37,59,82,99,115,133,165,188,197".split(","))
    nodeList = list(nodeMap)
    lengths = [str(graph[node]["length"]) for node in nodeList]
    #lengths = [str(graph[node]["length"]) for node in nodeList]
    lenString = ",".join(lengths)
    print("networkx result")
    pp.pprint(dijkstraPathNetworkx(graph, nodeList))
    print("my result")
    pp.pprint(lenString)

    #pp.pprint(list(nodeMap))
    #sorted(graph, key= lambda x: graph[x]['length'])
    #smallGraph = more_itertools.take(10, graph.items())
    ##smallGraphLengths = [smallGraph[key]['length'][0] for key in smallGraph]
    ##pp.pprint(smallGraphLengths)
    #for key in smallGraph:
    #    print(key[0])
    #    print(graph[key[0]]['length'])
    #    #print(smallGraph[key]['length'])




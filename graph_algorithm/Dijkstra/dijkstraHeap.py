import collections
from pathlib import Path
import pprint
import sys
import networkx as nx
import matplotlib.pyplot as plt
import math
#import more_itertools
#import heapq
pp = pprint.PrettyPrinter(width=41, compact=True)
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/dijkstraChallenge.txt"
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/testCase1.txt"

def insert(heap, key):
    if heap:
        heap.append(key)
        childIndex = len(heap) - 1
        parentIndex = math.ceil(childIndex / 2) - 1
        while heap[parentIndex][0] > heap[childIndex][0] and childIndex != 0:
            heap[parentIndex][0], heap[childIndex][0] = heap[childIndex][0], heap[parentIndex][0]
            childIndex = parentIndex
            parentIndex = math.ceil(childIndex / 2) - 1
    else:
        heap.append(key)
        childIndex = 0

    return heap, childIndex

def extractMin(heap):
    minimumElement = heap[0]
    heap[0] = heap.pop()
    parentIndex = 0
    firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2

    while heap[parentIndex] > heap[firstChildIndex] or heap[parentIndex] > heap[secondChildIndex]:
        if heap[firstChildIndex] < heap[secondChildIndex]:
            heap[firstChildIndex], heap[parentIndex] = heap[parentIndex], heap[firstChildIndex]
            parentIndex = firstChildIndex
            firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2
        elif heap[secondChildIndex] <= heap[firstChildIndex]:
            heap[secondChildIndex], heap[parentIndex] = heap[parentIndex], heap[secondChildIndex]
            parentIndex = secondChildIndex
            firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2

        if secondChildIndex >= len(heap) -1:
            break
    return minimumElement, heap

def delete(heap, index):
    lastIndex = len(heap) - 1
    if index == lastIndex:
        deletedElement = heap.pop()
        return deletedElement, heap
    if index == 0:
        deletedElement, heap = extractMin(heap)
        return deletedElement, heap
    firstChildIndex, secondChildIndex = 2 * index + 1, 2 * index + 2
    if secondChildIndex <= 


def createGraph(fileName):
    graph = collections.defaultdict(lambda : {'children': {}, 'length': 1000000, 'indexInHeap': None})
    with open(fileName) as f:
        for line in f:
            test = line.split()
            #print(test)
            for child in test[1:]:
                node, weight = map(int, child.split(','))
                graph[int(test[0])]['children'][node] = weight
    #pp.pprint(graph)
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
def createIndicesInHeap(heap):
    indicesInHeap = {}
    for i, element in enumerate(heap):
        indicesInHeap[element] = i
    return indicesInHeap

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
    seenVertex = {}
    graph[1]['length'] = 0
    graph[1]['indexInHeap'] = 0
    heap = []
    for vertex in graph:
        heap, _ = insert(heap, (graph[vertex]['length'], vertex))
    pp.pprint(heap)
    deletedElement, heap = delete(heap, 5)
    print(f"deleted elem {deletedElement}")
    pp.print(heap)

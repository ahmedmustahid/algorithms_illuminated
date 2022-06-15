import collections
from pathlib import Path
import pprint
import sys
pp = pprint.PrettyPrinter(width=41, compact=True)


graph = collections.defaultdict(lambda : {'children': {}, 'length': 1000000})
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/testCase1.txt"


with open(fileName) as f:
    for line in f:
        test = line.split()
        #print(test)
        for child in test[1:]:
            node, weight = map(int, child.split(','))
            graph[int(test[0])]['children'][node] = weight
pp.pprint(graph)
if __name__ == "__main__":
    seenNodes = {1}
    nodesEdgesWeights = {}
    graph[1]['length']= 0
    while len(seenNodes) != len(graph):
        for parent in graph:
            if parent in seenNodes:
                for child in graph[parent]["children"]:
                    if not child in seenNodes:
                        nodeEdge = (parent, child)
                        #weight =graph[parent]["children"][child]
                        nodesEdgesWeights[nodeEdge] = graph[parent]["length"] + graph[parent]["children"][child]

            minParent ,minChild = min(nodesEdgesWeights, key= nodesEdgesWeights.get)
            minWeightValue = min(nodesEdgesWeights.values())
            graph[minChild]["length"] = minWeightValue + graph[minParent]["length"]
            seenNodes.add(minChild)
            nodesEdgesWeights.pop((minParent,minChild))


pp.pprint(graph)





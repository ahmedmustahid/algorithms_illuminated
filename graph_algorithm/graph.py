from pathlib import Path
import pprint
import collections
import sys

pp = pprint.PrettyPrinter(width=41, compact=True)
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/scc/test_cases/testCase1.txt"
#fileName = Path.home()/"work/sccTestCase.txt"

#graphDict = {}
#graph = collections.defaultdict(lambda: {'g': set(), 's': False, 't': None, 'u': None })
graph = collections.defaultdict(lambda: {'g': [], 's': False, 'label': 0})
#graph = collections.defaultdict(lambda: {'g': [], 's': False, 't': None, 'u': None })
for line in open(fileName, "r"):
    #print(line)
    k, v = map(int, line.split())
    #print(f"{k}:{v}")
    if k != v:
        graph[k]['g'].append(v)
    #graph[k]['g'].add(v)


pp.pprint(graph)
#for k in graph:
#    pp.pprint(graph[k])
#    #print(k)
    
#for key in graph.keys():
#    print(key)
#    break

currentLabel = len(graph)
print(f"currentLabel {currentLabel}")

for key in graph.keys():
    stack = [key]
    exploredNodes = [] 
    while stack:
        poppedNode = stack.pop()
        #pp.pprint(v)
        if not graph[poppedNode]['s']:
            graph[poppedNode]['s'] = True
            exploredNodes.append(poppedNode)
    
            for w in graph[poppedNode]['g']:
                stack.append(w)

    while exploredNodes:
        exploredNode = exploredNodes.pop()
        graph[exploredNode]['label'] = currentLabel
        currentLabel = currentLabel - 1


for key in graph.keys():
    print(f"{key}:label {graph[key]['label']}")
#pp.pprint(graph)

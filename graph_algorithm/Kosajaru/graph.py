from pathlib import Path
import pprint
import collections
import sys
import tracemalloc 


pp = pprint.PrettyPrinter(width=41, compact=True)

tracemalloc.start()
def graphFromFile(fileName):
    graph = collections.defaultdict(lambda: {'children': [], 'explored': False, 'label': 0})
    for line in open(fileName, "r"):
        k, v = map(int, line.split())
        if k != v:
            graph[k]['children'].append(v)
    return graph
fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/scc/test_cases/testCase1.txt"
graph = graphFromFile(fileName)
currentLabel = len(graph)
dfsNum = 0

def reversedGraph(graph):
    reversedGraph = collections.defaultdict(lambda: {'children': [], 'explored': False, 'label': 0})
    for vertex in graph:
        for child in graph[vertex]['children']:
            reversedGraph[child]['children'].append(vertex)
    return reversedGraph

def dfs(vertex):
    global currentLabel
    global dfsNum
    #print(f"{dfsNum} entering at {vertex}")
    print(f"entering at {vertex}")
    dfsNum = dfsNum + 1
    graph[vertex]['explored'] = True
    for child in graph[vertex]['children']:
        print(f"child {child} of vertex {vertex}")
        if not graph[child]['explored']:
            dfs(child)
        else:
            print(f"child {child} already explored")
    graph[vertex]['label'] = currentLabel
    currentLabel = currentLabel -1
    print(f"exiting from {vertex}")

def toposort():
    for vertex in graph:
        dfs(vertex)


if __name__=="__main__":
    print(tracemalloc.get_traced_memory())
    dfs(vertex=2)
    pp.pprint(graph)
    pp.pprint(reversedGraph(graph))
    tracemalloc.stop()






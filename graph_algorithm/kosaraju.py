from pathlib import Path
import pprint
import collections
import sys
import tracemalloc 


pp = pprint.PrettyPrinter(width=41, compact=True)

#tracemalloc.start()
def graphFromFile(fileName):
    graph = collections.defaultdict(lambda: {'children': [], 'explored': False, 'label': 0})
    for line in open(fileName, "r"):
        k, v = map(int, line.split())
        if k != v:
            graph[k]['children'].append(v)
    return graph
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/scc/test_cases/testCase1.txt"
fileName = Path.cwd()/"testCase2.txt"
graph = graphFromFile(fileName)
currentLabel = len(graph)
dfsNum = 0
labelDict = dict.fromkeys(range(currentLabel, 0, -1))

def reversedGraph(graph):
    reversedGraph = collections.defaultdict(lambda: {'children': [], 'explored': False})
    for vertex in graph:
        for child in graph[vertex]['children']:
            reversedGraph[child]['children'].append(vertex)
    return reversedGraph

def dfs(graph, vertex):
    global currentLabel
    global dfsNum
    #print(f"{dfsNum} entering at {vertex}")
    print(f"entering at {vertex}")
    dfsNum = dfsNum + 1
    graph[vertex]['explored'] = True
    for child in graph[vertex]['children']:
        print(f"child {child} of vertex {vertex}")
        if not graph[child]['explored']:
            dfs(graph, child)
        else:
            print(f"child {child} already explored")
    graph[vertex]['label'] = currentLabel
    labelDict[currentLabel] = vertex
    currentLabel = currentLabel -1
    print(f"exiting from {vertex}")


def iterativeDFS(graph):
    stack = [6]
    exploreOrder = []
    while stack:
        poppedNode = stack.pop()
        if not graph[poppedNode]['explored']:
            graph[poppedNode]['explored'] = True
            stack += graph[poppedNode]['children']
            exploreOrder.append(poppedNode)
            #for child in graph[poppedNode]['children']:
    print(exploreOrder)



def toposort():
    for vertex in graph:
        if not graph[vertex]['explored']:
            print(f"in toposort {vertex}")
            dfs(graph, vertex)


if __name__=="__main__":
    #print(tracemalloc.get_traced_memory())
    #dfs(vertex=2)
    #pp.pprint(reversedGraph(graph))
    #toposort()
    #tracemalloc.stop()
    #pp.pprint(labelDict)
    pp.pprint(graph)
    iterativeDFS(graph)






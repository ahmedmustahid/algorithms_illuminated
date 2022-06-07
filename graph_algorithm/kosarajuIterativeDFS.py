from pathlib import Path
import pprint
import collections
import sys
#import tracemalloc 


pp = pprint.PrettyPrinter(width=41, compact=True)

#tracemalloc.start()
def graphFromFile(fileName):
    graph = collections.defaultdict(lambda: {'children': [], 'explored': False, 'label': 0})
    for line in open(fileName, "r"):
        k, v = map(int, line.split())
        if k != v:
            graph[k]['children'].append(v)
    return graph
#fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/testCases/test1.txt"
#fileName = Path.cwd()/"testCase2.txt"

#Challenge case 
fileName = Path.home()/"work/sccTestCase.txt"

graph = graphFromFile(fileName)
currentLabel = len(graph)
dfsNum = 0
#labelOrderedDict = dict.fromkeys(range(currentLabel, 0, -1))
labelOrderedDict = collections.OrderedDict()
numSCC = 0
scc = collections.defaultdict(list)

def reverseGraph(graph):
    reversedGraph = collections.defaultdict(lambda: {'children': [], 'explored': False, 'label':0})
    for vertex in graph:
        for child in graph[vertex]['children']:
            reversedGraph[child]['children'].append(vertex)
    for vertex in graph:
        if not vertex in reversedGraph:
            reversedGraph[vertex]['children']=[]
    return reversedGraph

def dfs(graph, vertex):
    global currentLabel
    global dfsNum
    #print(f"{dfsNum} entering at {vertex}")
    #print(f"entering at {vertex}")
    dfsNum = dfsNum + 1
    graph[vertex]['explored'] = True
    scc[numSCC].append(vertex)
    for child in graph[vertex]['children']:
        #print(f"child {child} of vertex {vertex}")
        if not graph[child]['explored']:
            dfs(graph, child)
        else:
            #print(f"child {child} already explored")
            pass
    graph[vertex]['label'] = currentLabel
    labelOrderedDict[vertex] = currentLabel
    currentLabel = currentLabel -1
    #print(f"exiting from {vertex}")


def iterativeDFS(graph, vertex):
    global currentLabel
    stack = [vertex]
    exploreOrder = []
    while stack:
        poppedNode = stack.pop()
        if not graph[poppedNode]['explored']:
            graph[poppedNode]['explored'] = True
            stack += graph[poppedNode]['children']
            exploreOrder.append(poppedNode)
    #return exploreOrder
    while exploreOrder:
        vertex = exploreOrder.pop()
        scc[numSCC].append(vertex)
        labelOrderedDict[vertex] = currentLabel
        graph[vertex]['label'] = currentLabel
        currentLabel = currentLabel - 1



def toposort(graph):
    for vertex in graph:
        if not graph[vertex]['explored']:
            #print(f"in toposort {vertex}")
            #dfs(graph, vertex)
            iterativeDFS(graph, vertex)


if __name__=="__main__":
    reversedGraph = reverseGraph(graph)
    toposort(graph=reversedGraph)
    #pp.pprint(reversedGraph)
    for vertex in reversedGraph:
        graph[vertex]['label'] = reversedGraph[vertex]['label']
    #pp.pprint(graph)
    #pp.pprint(labelOrderedDict)
    scc.clear()
    #sys.exit()
    for vertex, label in reversed(labelOrderedDict.items()):
        #print(vertex, label)
        if not graph[vertex]['explored']:
            numSCC = numSCC + 1
            #dfs(graph, vertex)
            iterativeDFS(graph, vertex)
    print(f"numSCC {numSCC}")
    #pp.pprint(scc)
    sccLengthsList = [ len(value) for _, value in scc.items() ]
    sccLengthsList = sorted(sccLengthsList, reverse=True)
    print(sccLengthsList[:5])






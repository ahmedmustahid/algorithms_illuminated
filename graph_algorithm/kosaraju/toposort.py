import time
import pprint
#from memory_profiler import profile
#import tracemalloc

#tracemalloc.start()

def graphFromFile(fileName):

    startTime = time.time()
    temp = "1" 
    d = {temp:[]}
    heads = []
    with open(fileName,"r") as f:
        for line in f:
            tail, head = line.split()

            if tail == head :
                continue  
            if temp == tail:
                d[temp].append(head)
                heads.append(head)
            else:
                temp = tail
                #d = {temp:[head]}
                d[temp] = [head]
                heads.append(head)
    
    for head in heads:
        if head not in d:
            d[head] = []
            #print(head)
            #break
    #pprint.pprint(d)
    #pprint.pprint(d[temp])
    print("--- %s seconds ---" % (time.time() - startTime))
    return d

#class TopoSort:
#    def __init__(graphDict, exploredNodeDict, topoSortNumDict):
#        self.graphDict = graphDict
#        self.exploredNodeDict = exploredNodeDict
#        self.topoSortNumDict = topoSortNumDict
#        self.depth = len(graphDict)
#
#    def dfstopo(self):
#fileName ="scc/sccChallenge.txt"
fileName ="scc/test_cases/testCase1.txt"
graphDict = graphFromFile(fileName)
exploredNodeDict = dict.fromkeys(graphDict, False)
toposortNum = dict.fromkeys(graphDict)
#depth = len(graphDict)

def dfstopo(node):

    global depth
    #global graphDict
    # if node not in graphDict:
    #     return
    if exploredNodeDict[node] is False:
        exploredNodeDict[node] = True
    else:
        return
    
    for adjacentNode in graphDict[node]:
        dfstopo(adjacentNode)
    
    toposortNum[node] = depth
    depth = depth - 1
    #print(depth)
    return 

def topoSort(graphDict):
    global depth
    depth = len(graphDict)
    for node in graphDict:
        if exploredNodeDict[node] is False:
            dfstopo(node)

#if __name__=="__main__":


#pprint.pprint(exploredNodeDict)
#pprint.pprint(toposortNum)
#print(f"total number of nodes {depth}")
#dfstopo(graphDict=graphDict, node = '1')

topoSort(graphDict=graphDict)

#mygraph = graphFromFile(fileName)
# if '416780' in graphDict.keys():
#     print("yes")
# else:
#     print("no")

# print(tracemalloc.get_traced_memory())
# tracemalloc.stop()
pprint.pprint(graphDict)
pprint.pprint(exploredNodeDict)

pprint.pprint(toposortNum)
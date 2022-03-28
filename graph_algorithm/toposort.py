import time
import pprint
def graphFromFile(fileName):

    startTime = time.time()
    temp = "1" 
    d = {temp:[]}
    with open(fileName,"r") as f:
        for line in f:
            tail, head = line.split()

            if tail == head :
                continue  
            if temp == tail:
                d[temp].append(head)
            else:
                temp = tail
                #d = {temp:[head]}
                d[temp] = [head]
    
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
fileName ="scc/test_cases/testCase1.txt"
graphDict = graphFromFile(fileName)
exploredNodeDict = dict.fromkeys(graphDict, False)
toposortNum = dict.fromkeys(graphDict)
#depth = len(graphDict)

def dfstopo(graphDict,node):

    global depth
    if exploredNodeDict[node] is False:
        exploredNodeDict[node] = True
    else:
        return
    
    for adjacentNode in graphDict[node]:
        dfstopo(graphDict, adjacentNode)
    
    toposortNum[node] = depth
    depth = depth - 1

    return 

def topoSort(graphDict):
    global depth
    depth = len(graphDict)
    for node in graphDict.keys():
        if exploredNodeDict[node] is False:
            dfstopo(graphDict,node)

#if __name__=="__main__":


#pprint.pprint(exploredNodeDict)
#pprint.pprint(toposortNum)
#print(f"total number of nodes {depth}")
#dfstopo(graphDict=graphDict, node = '1')
topoSort(graphDict=graphDict)
pprint.pprint(graphDict)
pprint.pprint(exploredNodeDict)

pprint.pprint(toposortNum)
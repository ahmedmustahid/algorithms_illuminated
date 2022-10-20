import enum
from linkedList import LinkedList
#import queue

def dfs(graphDict, nodeData):
    headsExploredDictionary[nodeData] = True
    linkedListOfExploredNode = graphDict[nodeData]

    for i, node in enumerate(linkedListOfExploredNode):
        if i > 0 and headsExploredDictionary[node.data] == False:
            dfs(graphDict, node.data)
    
    print(headsExploredDictionary)
    return



allLists = [["s","a","b"], ["a","s","c"], ["b","s","c"], ["c","a","b","e","d"],["e","c","d"], ["d","c","e"]]
allLinkedLists = [LinkedList(givenList) for givenList in allLists]

allLinkedListsDict = {linkedList.head.data:linkedList for linkedList in allLinkedLists}
headsExploredDictionary = {linkedList.head.data:linkedList.head.explored for linkedList in allLinkedLists}

dfs(allLinkedListsDict, nodeData="s")

print(allLinkedListsDict)
print(headsExploredDictionary)




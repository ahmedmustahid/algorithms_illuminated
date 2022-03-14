from linkedList import LinkedList
import queue

allLists = [["s","a","b"], ["a","s","c"], ["b","s","c"], ["c","a","b","e","d"],["e","c","d"], ["d","c","e"]]
allLinkedLists = [LinkedList(givenList) for givenList in allLists]

allLinkedListsDict = {linkedList.head.data:linkedList for linkedList in allLinkedLists}
headsExploredDictionary = {linkedList.head.data:linkedList.head.explored for linkedList in allLinkedLists}
#headsExploredDictionary["s"] = True
print(allLinkedListsDict)
print(headsExploredDictionary)


exploredNodes = []
exploredNodes.append("s")
while len(exploredNodes) != 0:
    removedNodeData = exploredNodes.pop()
    
    if removedNodeData in allLinkedListsDict:
        linkedList = allLinkedListsDict[removedNodeData]

        _ = iter(linkedList)
        for neighbourNode in linkedList:
            if headsExploredDictionary[neighbourNode.data] is False:
                headsExploredDictionary[neighbourNode.data] = True
                exploredNodes.append(neighbourNode.data)

print(headsExploredDictionary) 






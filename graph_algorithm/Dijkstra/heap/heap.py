import heapq
class Heap:
    def __init__(self, heap: list):
        self.heap = heap
        self.indicesDict = {}
    @staticmethod
    def getParentIndex(childIndex):
        if childIndex % 2 == 0: #even
            parentIndex = childIndex // 2 - 1
        else:
            parentIndex = childIndex // 2
        return parentIndex


    def swap(self, indx1, indx2):
        self.heap[indx2], self.heap[indx1] = self.heap[indx1], self.heap[indx2]
        self.indicesDict[self.heap[indx2]] = indx1
        self.indicesDict[self.heap[indx1]] = indx2

    def insert(self, elem: int):
        if len(self.heap)==0:
            self.heap.append(elem)
            self.indicesDict[elem] = 0
        else:
            self.heap.append(elem)
            childIndex = len(self.heap) - 1
            parentIndex = Heap.getParentIndex(childIndex)
            while childIndex != 0 and self.heap[parentIndex] > self.heap[childIndex]:
                #self.heap[parentIndex], self.heap[childIndex] = self.heap[childIndex], self.heap[parentIndex]
                self.swap(parentIndex, childIndex)
                childIndex = parentIndex
                parentIndex = Heap.getParentIndex(childIndex)
        return self.heap
    
    def createIndicesDict(self):
        self.indicesDict = {elem:indx for indx, elem in enumerate(self.heap)}


    def swapLastElemWithParent(self, parentIndex):
        lastIndex = len(self.heap) - 1
        getChildrenIndices = lambda parentIndex : (2 * parentIndex + 1, 2 * parentIndex + 2)
        child1Index, child2Index = getChildrenIndices(parentIndex)
        returnSmallerChildIndex = lambda x,y: (x if self.heap[x]<self.heap[y] else y)
        if child2Index <= lastIndex:
            smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
            while self.heap[parentIndex] > self.heap[smallerChildIndex]:
                #self.heap[parentIndex], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[parentIndex]
                self.swap(parentIndex, smallerChildIndex)
                parentIndex = smallerChildIndex
                child1Index, child2Index = getChildrenIndices(parentIndex)
                if child2Index <= lastIndex:
                    #smallerChild = min(self.heap[child1Index], self.heap[child2Index])
                    smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
                elif child1Index <= lastIndex:
                    smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                    if parentIndex != smallerElemIndex:
                        self.swap(smallerElemIndex, parentIndex)
                    #return root, self.heap
        elif child1Index <= lastIndex:
            smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
            if parentIndex != smallerElemIndex:
                #self.heap[parentIndex], self.heap[smallerElemIndex] = self.heap[smallerElemIndex], self.heap[parentIndex]
                self.swap(smallerElemIndex, parentIndex)

    def delete(self, key):
        if key in self.indicesDict:
            indx = self.indicesDict.pop(key)
            #self.heap[indx] = self.heap.pop()
            self.swapLastElemWithParent(parentIndex=indx)
        return key, self.heap

    def extractMin(self) -> (int,list):
        if len(self.heap) == 0:
            raise Exception("Empty heap")
        else:
            root = self.heap[0]
            if len(self.heap)==1:
                return root, []
            elif len(self.heap) > 1:
                root = self.heap[0]
                self.heap[0] = self.heap.pop()
                self.swapLastElemWithParent(parentIndex=0)
        return root, self.heap
'''
                parentIndex = 0
                lastIndex = len(self.heap) - 1
                getChildrenIndices = lambda parentIndex : (2 * parentIndex + 1, 2 * parentIndex + 2)
                child1Index, child2Index = getChildrenIndices(parentIndex)
                returnSmallerChildIndex = lambda x,y: (x if self.heap[x]<self.heap[y] else y)
                if child2Index <= lastIndex:
                    smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
                    while self.heap[parentIndex] > self.heap[smallerChildIndex]:
                        #self.heap[parentIndex], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[parentIndex]
                        self.swap(parentIndex, smallerChildIndex)
                        parentIndex = smallerChildIndex
                        child1Index, child2Index = getChildrenIndices(parentIndex)
                        if child2Index <= lastIndex:
                            #smallerChild = min(self.heap[child1Index], self.heap[child2Index])
                            smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
                        elif child1Index <= lastIndex:
                            smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                            if parentIndex != smallerElemIndex:
                                #self.heap[parentIndex], self.heap[smallerElemIndex] = self.heap[smallerElemIndex], self.heap[parentIndex]
                                self.swap(smallerElemIndex, parentIndex)
                            #return root, self.heap
                elif child1Index <= lastIndex:
                    smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                    if parentIndex != smallerElemIndex:
                        #self.heap[parentIndex], self.heap[smallerElemIndex] = self.heap[smallerElemIndex], self.heap[parentIndex]
                        self.swap(smallerElemIndex, parentIndex)
                    return root, self.heap
                return root, self.heap
'''




if __name__=="__main__":
    h = []
    hp = Heap(h)
    #temp = [4, 4, 4, 9, 9, 11, 12, 13]
    #temp = [4, 11, 9, 13, 4, 12, 9, 4]
    temp = list(map(int, "7 10 20 3 4 49 50".split()))
    #random.shuffle(temp)
    print("before ", temp)
    #for t in temp:
    #    heapq.heappush(h, t)
    for t in temp:
        hp.insert(t)
        print(hp.heap)
    heapq.heapify(temp)
    print("from python", temp)
    print("from me ",h)
    #temp = [4]
    #temp = [4,5,13]
    print(f"heap inside class {hp.heap}")
    minimumVal, _ = hp.extractMin()
    print(minimumVal)
    #print(resultHeap)
    print(hp.heap)

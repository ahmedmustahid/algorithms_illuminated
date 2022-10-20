import heapq
class Heap:
    def __init__(self, heap: list):
        self.heap = heap
    @staticmethod
    def getParentIndex(childIndex):
        if childIndex % 2 == 0: #even
            parentIndex = childIndex // 2 - 1
        else:
            parentIndex = childIndex // 2
        return parentIndex

    def insert(self, elem: int):
        if len(self.heap)==0:
            self.heap.append(elem)
        else:
            self.heap.append(elem)
            childIndex = len(self.heap) - 1
            parentIndex = Heap.getParentIndex(childIndex)
            while childIndex != 0 and self.heap[parentIndex] > self.heap[childIndex]:
                self.heap[parentIndex], self.heap[childIndex] = self.heap[childIndex], self.heap[parentIndex]
                childIndex = parentIndex
                parentIndex = Heap.getParentIndex(childIndex)
        return self.heap

    def extractMin(self) -> (int,list):
        if len(self.heap) == 0:
            raise Exception("Empty self.heap")
        else:
            root = self.heap[0]
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop()
            elif len(self.heap) == 1:
                root = self.heap.pop()
                return root, self.heap
    
            parentIndex = 0
    
            getChildrenIndices = lambda parentIndex : (2 * parentIndex + 1, 2 * parentIndex + 2)
            #child1Index = 2 * parentIndex + 1
            #child2Index = 2 * parentIndex + 2
            lastIndex = len(self.heap) - 1
            child1Index, child2Index = getChildrenIndices(parentIndex)
            returnSmallerChildIndex = lambda x,y: (x if self.heap[x]<self.heap[y] else y)
            if child2Index <= lastIndex:
                #smallerChild = min(self.heap[child1Index], self.heap[child2Index])
                smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
            elif child1Index <= lastIndex:
                smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                if parentIndex != smallerElemIndex:
                    self.heap[parentIndex], self.heap[smallerElemIndex] = self.heap[smallerElemIndex], self.heap[parentIndex]
                return root, self.heap
            else:
                return root, self.heap
    
            while self.heap[parentIndex] > self.heap[smallerChildIndex]:
                self.heap[parentIndex], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[parentIndex]
                parentIndex = smallerChildIndex
                child1Index, child2Index = getChildrenIndices(parentIndex)
                if child2Index <= lastIndex:
                    #smallerChild = min(self.heap[child1Index], self.heap[child2Index])
                    smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
                elif child1Index <= lastIndex:
                    smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                    if parentIndex != smallerElemIndex:
                        self.heap[parentIndex], self.heap[smallerElemIndex] = self.heap[smallerElemIndex], self.heap[parentIndex]
                    return root, self.heap
                else:
                    break
            return root, self.heap





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

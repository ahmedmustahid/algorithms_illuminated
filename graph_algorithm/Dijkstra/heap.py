import heapq

def getParentIndex(childIndex):
    if childIndex % 2 == 0: #even
        parentIndex = childIndex // 2 - 1
    else:
        parentIndex = childIndex // 2
    return parentIndex


def insert(heap: list, elem):
    if len(heap)==0:
        heap.append(elem)
    else:
        heap.append(elem)
        childIndex = len(heap) - 1

        parentIndex = getParentIndex(childIndex)

        while childIndex != 0 and heap[parentIndex] > heap[childIndex]:
            heap[parentIndex], heap[childIndex] = heap[childIndex], heap[parentIndex]
            childIndex = parentIndex
            parentIndex = getParentIndex(childIndex)

    return heap

def extractMin(heap: list) -> (int,list):
    if len(heap) == 0:
        raise Exception("Empty heap")
    else:
        root = heap[0]
        if len(heap) > 1:
            heap[0] = heap.pop()
        elif len(heap) == 1:
            root = heap.pop()
            return root, heap

        parentIndex = 0

        getChildrenIndices = lambda parentIndex : (2 * parentIndex + 1, 2 * parentIndex + 2)
        #child1Index = 2 * parentIndex + 1
        #child2Index = 2 * parentIndex + 2
        lastIndex = len(heap) - 1
        child1Index, child2Index = getChildrenIndices(parentIndex)
        returnSmallerChildIndex = lambda x,y: (x if heap[x]<heap[y] else y)
        if child2Index <= lastIndex:
            #smallerChild = min(heap[child1Index], heap[child2Index])
            smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
        elif child1Index <= lastIndex:
            smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
            if parentIndex != smallerElemIndex:
                heap[parentIndex], heap[smallerElemIndex] = heap[smallerElemIndex], heap[parentIndex]
            return root, heap
        else:
            return root, heap

        while heap[parentIndex] > heap[smallerChildIndex]:
            heap[parentIndex], heap[smallerChildIndex] = heap[smallerChildIndex], heap[parentIndex]
            parentIndex = smallerChildIndex
            child1Index, child2Index = getChildrenIndices(parentIndex)
            if child2Index <= lastIndex:
                #smallerChild = min(heap[child1Index], heap[child2Index])
                smallerChildIndex = returnSmallerChildIndex(child1Index, child2Index)
            elif child1Index <= lastIndex:
                smallerElemIndex = returnSmallerChildIndex(parentIndex, child1Index)
                if parentIndex != smallerElemIndex:
                    heap[parentIndex], heap[smallerElemIndex] = heap[smallerElemIndex], heap[parentIndex]
                return root, heap
            else:
                break
        return root, heap





if __name__=="__main__":
    h = []
    #temp = [4, 4, 4, 9, 9, 11, 12, 13]
    #temp = [4, 11, 9, 13, 4, 12, 9, 4]
    temp = list(map(int, "7 10 20 3 4 49 50".split()))
    #random.shuffle(temp)
    print("before ", temp)
    #for t in temp:
    #    heapq.heappush(h, t)
    for t in temp:
        insert(h, t)
        print(h)
    heapq.heapify(temp)
    print("from python", temp)
    print("from me ",h)
    
    #temp = [4]
    #temp = [4,5,13]

    minimumVal, resultHeap = extractMin(temp)
    print(minimumVal)
    print(resultHeap)

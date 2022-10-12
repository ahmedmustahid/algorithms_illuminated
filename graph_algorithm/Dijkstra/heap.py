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

        while heap[parentIndex] > heap[childIndex] and childIndex != 0:
            heap[parentIndex], heap[childIndex] = heap[childIndex], heap[parentIndex]
            childIndex = parentIndex
            parentIndex = getParentIndex(childIndex)

    return heap




if __name__=="__main__":
    h = []
    #temp = [4, 4, 4, 9, 9, 11, 12, 13]
    temp = [4, 11, 9, 13, 4, 12, 9, 4]
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

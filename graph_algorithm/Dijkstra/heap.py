import heapq
import random
import math

def getParentIndex(childIndex):
    if childIndex % 2 == 0: #even
        parentIndex = childIndex /2 - 1
    else:
        parentIndex = math.floor(childIndex / 2)
    return parentIndex


def insert(heap: list, elem):
    if len(heap)==0:
        heap.append(elem)
    else:
        heap.append(elem)
        childIndex = len(heap) - 1

        parentIndex = getParentIndex(childIndex)

        while heap[parentIndex] < heap[childIndex]:
            heap[parentIndex], heap[childIndex] = heap[childIndex], heap[parentIndex]




if __name__=="__main__":
    h = []
    #temp = [4, 4, 4, 9, 9, 11, 12, 13]
    temp = [4, 11, 9, 13, 4, 12, 9, 4]
    #random.shuffle(temp)
    print("before ", temp)
    for t in temp:
        heapq.heappush(h, t)
    heapq.heapify(temp)
    print(temp)
    print(h)

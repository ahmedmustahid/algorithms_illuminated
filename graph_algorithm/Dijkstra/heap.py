import math
import pprint
import heapq
pp = pprint.PrettyPrinter(width=41, compact=True)
def insert(heap, key):
    if heap:
        heap.append(key)
        childIndex = len(heap) - 1
        parentIndex = math.ceil(childIndex / 2) - 1
        while heap[parentIndex] > heap[childIndex] and childIndex != 0:
            heap[parentIndex], heap[childIndex] = heap[childIndex], heap[parentIndex]
            childIndex = parentIndex
            parentIndex = math.ceil(childIndex / 2) - 1
    else:
        heap.append(key)

    return heap

if __name__=="__main__":
    keys = list(range(9,0,-1))
    print("original keys")
    pp.pprint(keys)
    heap = []
    for key in keys:
        heap = insert(heap, key)
        #pp.pprint(heap)
    print("my heap insertion")
    pp.pprint(heap)
    print("python heapify")
    heapq.heapify(keys)
    pp.pprint(keys)

    print("applying heapify to my heap insertion")
    heapq.heapify(heap)
    pp.pprint(heap)

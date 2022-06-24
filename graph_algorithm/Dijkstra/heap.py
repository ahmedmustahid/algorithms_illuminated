import math
import pprint
import heapq
import time
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

def extractMin(heap):
    minimumElement = heap[0]
    heap[0] = heap.pop()
    parentIndex = 0
    firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2

    while heap[parentIndex] > heap[firstChildIndex] or heap[parentIndex] > heap[secondChildIndex]:
        if heap[firstChildIndex] < heap[secondChildIndex]:
            heap[firstChildIndex], heap[parentIndex] = heap[parentIndex], heap[firstChildIndex]
            parentIndex = firstChildIndex
            firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2
        elif heap[secondChildIndex] <= heap[firstChildIndex]:
            heap[secondChildIndex], heap[parentIndex] = heap[parentIndex], heap[secondChildIndex]
            parentIndex = secondChildIndex
            firstChildIndex, secondChildIndex = 2 * parentIndex + 1, 2 * parentIndex + 2

        if secondChildIndex >= len(heap) -1:
            break
    return minimumElement, heap

if __name__=="__main__":
    keys = list(range(9,0,-1))
    print("original keys")
    pp.pprint(keys)
    start = time.time()
    heap = []
    for key in keys:
        heap = insert(heap, key)
        #pp.pprint(heap)
    print(f"time for my heap insert implementation {time.time() - start}")
    print("my heap insertion")
    pp.pprint(heap)
    print("python heapify")
    start = time.time()
    heapq.heapify(keys)
    print(f"time for python heapify implementation {time.time() - start}")
    pp.pprint(keys)

    print("applying heapify to my heap insertion")
    heapq.heapify(heap)
    pp.pprint(heap)

    heap2 = heap[:]

    minimumElement, newHeap = extractMin(heap)
    print(f"minimumElement my implementation {minimumElement}")
    print("new heap my implementation")
    pp.pprint(newHeap)

    minimumElementHeapq = heapq.heappop(heap2)
    print(f"minimumElement heapq {minimumElementHeapq}")
    print("new heap heapq implementation")
    pp.pprint(heap2)

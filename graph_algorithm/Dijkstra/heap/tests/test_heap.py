#from pathlib import Path
import heapq
import os, sys
sys.path.append(os.path.abspath(os.path.join("../..","heap")))
from heap import Heap

class Testheap:
    hp = Heap([])
    #temp = []
    def insertAll(self, givenHeap):
        for t in givenHeap:
            self.hp.insert(t)

    
    def test_heapInsert(self):
        temp = list(map(int, "7 10 20 3 4 49 50".split()))
        self.insertAll(givenHeap=temp)
        heapq.heapify(temp)
        assert self.hp.heap == temp
    
    def test_heapExtractMin(self):
        temp = list(map(int, "7 10 20 3 4 49 50".split()))
        heapq.heapify(temp)
        self.hp.heap = temp[:]

        minFromPythonHeapq = heapq.heappop(temp)
        minFromMine, outputHeap = self.hp.extractMin()
        assert minFromMine == minFromPythonHeapq
        assert outputHeap == temp

    def test_isHeap(self):
        temp = list(map(int, "7 10 20 3 4 49 50".split()))
        assert Heap.isHeap(temp) == False
        #assert Heap
        heapq.heapify(temp)
        assert Heap.isHeap(temp) == True

        temp = list(range(100,3,-1))
        assert Heap.isHeap(temp) == False
        heapq.heapify(temp)
        assert Heap.isHeap(temp) == True

        temp = [0,2]
        assert Heap.isHeap(temp) == True

        temp = [100,1, 4]
        assert Heap.isHeap(temp) == False

    
    def test_delete(self):
        temp = list(map(int, "7 10 20 3 4 49 50".split()))
        heapq.heapify(temp)
        self.hp.heap = temp[:]
        self.hp.createIndicesDict()
        k, _ = self.hp.delete(key=20)

        
        assert k == 20
        assert Heap.isHeap(self.hp.heap) == True
        
        
        temp = list(range(100,3,-1))
        heapq.heapify(temp)
        self.hp.heap = temp[:]
        self.hp.createIndicesDict()
        k, _ = self.hp.delete(key=20)

        assert k == 20
        assert Heap.isHeap(self.hp.heap) == True
    
        self.hp.insert(elem=20)
        assert Heap.isHeap(self.hp.heap) == True



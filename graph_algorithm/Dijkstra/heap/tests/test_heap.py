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
        #temp.sort()
        heapq.heapify(temp)
        self.hp.heap = temp[:]

        minFromPythonHeapq = heapq.heappop(temp)
        minFromMine, outputHeap = self.hp.extractMin()
        assert minFromMine == minFromPythonHeapq
        assert outputHeap == temp




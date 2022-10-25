#from pathlib import Path
import heapq
import os, sys
#sys.path.append("/home/ahmed/work/algorithms_illuminated/graph_algorithm/Dijkstra")
#from heap import HeapKeyVal as Heap
from Dijkstra.heap.heapKeyVal import Heap


class Testheap:
    hp = Heap([])
    #temp = []
    def insertAll(self, givenHeap):
        for t in givenHeap:
            self.hp.insert(t)
    @staticmethod
    def get_char(c1: str,c2: int):
       for c in range(ord(c1), c2+1):
           yield chr(c)

    @staticmethod
    def convertToTuple(temp):
        tempC = [c for c in Testheap.get_char('a', len(temp))]
        return [(t,c) for t,c in zip(temp,tempC)]
        #return temp
    def listFromTuple(self, temp):
        return [a[0] for a in temp]
    def test_heapInsert(self):
        temp = list(map(int, "7 10 20 3 4 49 50".split()))
        temp = Testheap.convertToTuple(temp=temp)
        self.insertAll(givenHeap=temp)
        heap = self.listFromTuple(self.hp.heap)
        temp = self.listFromTuple(temp)
        heapq.heapify(temp)
        assert heap == temp
    
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



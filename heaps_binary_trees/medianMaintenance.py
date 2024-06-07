from heap import MinHeap, MaxHeap
from typing import Tuple, List
import statistics
# def getMedian(h1: MaxHeap, h2: MinHeap, x: int)-> int:


class MedianHeap:
    def __init__(self) -> None:
        self.h1 = MaxHeap()
        self.h2 = MinHeap()
        # self.y = -(2**31)
        self.z = 2**31  # actually h2[0]
        self.count = 0
        self.k = self.count // 2

    def insert(self, x: int):
        if self.h2.getSize() > 0:
            self.z = self.h2[0]
        if x < self.z:
            self.h1.insert(x)
        else:
            self.h2.insert(x)

        self.count += 1
        self.k = self.count // 2

        if self.h1.getSize() == self.k - 1 or self.h2.getSize() == self.k - 1:
            self.h1, self.h2 = self.rebalance(self.h1, self.h2)

    def getMedian(self) -> int:
        if self.count % 2 == 0:
            medianIdx = self.count / 2 - 1
        else:
            medianIdx = (self.count + 1) / 2 - 1

        if medianIdx <= self.h1.getSize() - 1:
            return self.h1[0]
        else:
            return self.h2[0]

    @staticmethod
    def rebalance(h1: MaxHeap, h2: MinHeap) -> Tuple[MaxHeap, MinHeap]:
        if h1.getSize() > h2.getSize():
            temp = h1.extract()
            h2.insert(temp)
        else:
            temp = h2.extract()
            h1.insert(temp)
        return h1, h2


if __name__ == "__main__":
    # fname = "median.txt"
    # with open(fname, "r") as f:
    #     for line in f:
    #         print(int(line), sep=",")

    elems = list(range(20))
    mh = MedianHeap()
    tmplist: List[int] = []

    for elem in elems:
        mh.insert(elem)
        tmplist.append(elem)

        print(f"tmpList {tmplist}")
        print(f"h1: {mh.h1}")
        print(f"h2: {mh.h2}")
        print(f"median {mh.getMedian()}")
        print(f"python median low:{statistics.median_low(tmplist)}")
        print("---------------------")

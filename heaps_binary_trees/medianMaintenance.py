from heap import MinHeap, MaxHeap
from typing import Tuple, List
import statistics
import random


class MedianHeap:
    def __init__(self) -> None:
        self.h1 = MaxHeap()
        self.h2 = MinHeap()
        self.z = 2**31  # actually h2[0]
        self.count = 0
        self.k = self.count // 2

    def insert(self, x: int):
        if len(self.h2) > 0:
            self.z = self.h2[0]
        if x < self.z:
            self.h1.insert(x)
        else:
            self.h2.insert(x)

        self.count += 1
        self.k = self.count // 2

        if len(self.h1) == self.k - 1 or len(self.h2) == self.k - 1:
            self.h1, self.h2 = self.rebalance(self.h1, self.h2)

    def getMedian(self) -> int:
        if self.count % 2 == 0:
            medianIdx = self.count / 2 - 1
        else:
            medianIdx = (self.count + 1) / 2 - 1

        if medianIdx <= len(self.h1) - 1:
            return self.h1[0]
        else:
            return self.h2[0]

    @staticmethod
    def rebalance(h1: MaxHeap, h2: MinHeap) -> Tuple[MaxHeap, MinHeap]:
        # print(":::::::::::::::::::::::::::")
        # print(f"maxheap {h1}")
        # print(f"minheap {h2}")
        # print("666666666666666666")
        if len(h1) > len(h2):
            temp = h1.extract()
            h2.insert(temp)
        else:
            temp = h2.extract()
            h1.insert(temp)
        # print(f"maxheap {h1}")
        # print(f"minheap {h2}")
        # print(":::::::::::::::::::::::::::")
        return h1, h2


if __name__ == "__main__":
    mh = MedianHeap()
    tmplist: List[int] = []

    elems = [random.randint(1, 10000) for _ in range(1000)]
    # elems = [
    #     578,
    #     193,
    #     354,
    #     66,
    #     678,
    #     870,
    #     848,
    #     649,
    #     151,
    #     225,
    #     113,
    #     267,
    #     257,
    #     934,
    #     614,
    #     977,
    #     967,
    #     291,
    #     190,
    #     306,
    #     539,
    #     522,
    #     134,
    #     145,
    #     190,
    #     58,
    # ]
    for i, elem in enumerate(elems):
        # print(f"{i}th elem to insert {elem}")
        mh.insert(elem)
        tmplist.append(elem)

        # print(f"tmpList {tmplist}")
        # print(f"h1: {mh.h1}")
        # print(f"h2: {mh.h2}")
        mymedian = mh.getMedian()
        print(f"median {mymedian}")
        pymedian = statistics.median_low(tmplist)
        print(f"python median low:{pymedian}")
        assert mymedian == pymedian
        print("---------------------")

    # elems = [1, 84, 13, 55, 11, 22, 7, 16, 27, 62, 46, 28, 27, 42, 95, 56]
    # for elem in elems:
    #     mh.insert(elem)
    #     tmplist.append(elem)

    #     print(f"tmpList {tmplist}")
    #     print(f"h1: {mh.h1}")
    #     print(f"h2: {mh.h2}")
    #     print(f"median {mh.getMedian()}")
    #     print(f"python median low:{statistics.median_low(tmplist)}")
    #     print("---------------------")

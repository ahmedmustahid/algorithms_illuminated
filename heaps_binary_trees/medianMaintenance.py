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
        if len(h1) > len(h2):
            temp = h1.extract()
            h2.insert(temp)
        else:
            temp = h2.extract()
            h1.insert(temp)

        return h1, h2


def testCase():
    mh = MedianHeap()
    tmplist: List[int] = []

    elems = [random.randint(1, 10000) for _ in range(1000)]

    for i, elem in enumerate(elems):
        mh.insert(elem)
        tmplist.append(elem)

        mymedian = mh.getMedian()
        print(f"{i}th median {mymedian}")
        pymedian = statistics.median_low(tmplist)
        print(f"python median low:{pymedian}")
        assert mymedian == pymedian
        print("---------------------")


def challengeCase() -> int:
    mh = MedianHeap()
    tmplist: List[int] = []
    medians: List[int] = []
    with open("median.txt", "r") as f:
        for i, line in enumerate(f):
            elem = int(line)
            tmplist.append(elem)
            mh.insert(elem)
            median = mh.getMedian()
            medians.append(median)
            # pymedian = statistics.median_low(tmplist)
            # assert pymedian == median
            # print(f"python median low:{pymedian}")
            print(f"{i}th median {median}")
    s = sum(medians)
    mod = s % 10000

    print(f"mod: {mod}")
    return mod


if __name__ == "__main__":
    challengeCase()

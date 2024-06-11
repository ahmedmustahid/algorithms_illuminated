from typing import Callable, List
# import math
# import random


class MinHeap:
    def __init__(self) -> None:
        self.container: List[int] = []
        self.getParentIdx: Callable[[int], int] = (
            lambda i: i // 2 if i % 2 != 0 else i // 2 - 1
        )

    def insert(self, elem: int) -> None:
        self.container.append(elem)

        childIdx = len(self.container) - 1
        parentIdx = self.getParentIdx(childIdx)
        child = self.container[childIdx]
        parent = self.container[parentIdx]

        while child < parent:
            self.container[childIdx], self.container[parentIdx] = parent, child
            childIdx = parentIdx
            if childIdx == 0:
                break
            parentIdx = self.getParentIdx(childIdx)
            child = self.container[childIdx]
            parent = self.container[parentIdx]

    # def swap(self, ):

    def extract(self) -> int:
        if len(self.container) == 1:
            extractedElem = self.container.pop()
            return extractedElem

        extractedElem = self.container[0]
        self.container[0] = self.container.pop()

        parentIndx = 0
        getChildren: Callable[[int], tuple[int, int]] = lambda i: (2 * i + 1, 2 * i + 2)
        child1Idx, child2Idx = getChildren(parentIndx)

        parent = self.container[parentIndx]
        child1, child2 = 2**31, 2**31

        if (child2Idx + 1) <= len(self.container):
            child1, child2 = self.container[child1Idx], self.container[child2Idx]
        elif (child1Idx + 1) == len(self.container):
            child1 = self.container[child1Idx]

        minChild = min(child1, child2)
        minChildIdx = child1Idx
        if minChild == child2:
            minChildIdx = child2Idx

        while parent > minChild:
            if minChildIdx > len(self.container) - 1:
                break
            self.container[parentIndx], self.container[minChildIdx] = minChild, parent
            parentIndx = minChildIdx
            child1Idx, child2Idx = getChildren(parentIndx)

            if (child2Idx + 1) <= len(self.container):
                child1, child2 = self.container[child1Idx], self.container[child2Idx]

                if (child2Idx + 1) == len(self.container):
                    # swap parent and minChild
                    minChild = min(child1, child2)
                    minChildIdx = child1Idx
                    if minChild == child2:
                        minChildIdx = child2Idx
                    self.container[parentIndx], self.container[minChildIdx] = (
                        minChild,
                        parent,
                    )
                    break
            elif (child1Idx + 1) == len(self.container):
                child1 = self.container[child1Idx]
                if parent > child1:
                    # swap parent and child
                    self.container[parentIndx], self.container[child1Idx] = (
                        child1,
                        parent,
                    )
                    break
            else:
                break

            minChild = min(child1, child2)
            minChildIdx = child1Idx
            if minChild == child2:
                minChildIdx = child2Idx

        return extractedElem

    def __len__(self):
        return len(self.container)

    def __getitem__(self, idx: int):
        return self.container[idx]

    def __str__(self) -> str:
        return ",".join([str(e) for e in self.container])


class MaxHeap:
    def __init__(self) -> None:
        self.container: List[int] = []
        self.getParentIdx: Callable[[int], int] = (
            lambda i: i // 2 if i % 2 != 0 else i // 2 - 1
        )

    def insert(self, elem: int) -> None:
        self.container.append(elem)

        childIdx = len(self.container) - 1
        parentIdx = self.getParentIdx(childIdx)
        child = self.container[childIdx]
        parent = self.container[parentIdx]

        while child > parent:
            self.container[childIdx], self.container[parentIdx] = parent, child
            childIdx = parentIdx
            if childIdx == 0:
                break
            parentIdx = self.getParentIdx(childIdx)
            child = self.container[childIdx]
            parent = self.container[parentIdx]
        assert self.container[0] == max(self.container)

    # def swap(self, ):

    def extract(self) -> int:
        if len(self.container) == 1:
            extractedElem = self.container.pop()
            return extractedElem

        extractedElem = self.container[0]
        self.container[0] = self.container.pop()

        parentIndx = 0
        getChildren: Callable[[int], tuple[int, int]] = lambda i: (2 * i + 1, 2 * i + 2)
        child1Idx, child2Idx = getChildren(parentIndx)

        parent = self.container[parentIndx]
        child1, child2 = -(2**31), -(2**31)

        if (child2Idx + 1) <= len(self.container):
            child1, child2 = self.container[child1Idx], self.container[child2Idx]
        elif (child1Idx + 1) == len(self.container):
            child1 = self.container[child1Idx]

        maxChild = max(child1, child2)
        maxChildIdx = child1Idx
        if maxChild == child2:
            maxChildIdx = child2Idx

        while parent < maxChild:
            if maxChildIdx > len(self.container) - 1:
                break
            self.container[parentIndx], self.container[maxChildIdx] = maxChild, parent
            parentIndx = maxChildIdx
            child1Idx, child2Idx = getChildren(parentIndx)

            if (child2Idx + 1) <= len(self.container):
                child1, child2 = self.container[child1Idx], self.container[child2Idx]

                if (child2Idx + 1) == len(self.container):
                    # swap parent and minChild
                    maxChild = max(child1, child2)
                    maxChildIdx = child1Idx
                    if maxChild == child2:
                        maxChildIdx = child2Idx
                    self.container[parentIndx], self.container[maxChildIdx] = (
                        maxChild,
                        parent,
                    )
                    break
            elif (child1Idx + 1) == len(self.container):
                child1 = self.container[child1Idx]
                if parent < child1:
                    # swap parent and child
                    self.container[parentIndx], self.container[child1Idx] = (
                        child1,
                        parent,
                    )
                    break
            else:
                break

            maxChild = max(child1, child2)
            maxChildIdx = child1Idx
            if maxChild == child2:
                maxChildIdx = child2Idx

        return extractedElem

    def __len__(self):
        return len(self.container)

    def __getitem__(self, idx: int):
        return self.container[idx]

    def __str__(self) -> str:
        return ",".join([str(e) for e in self.container])


if __name__ == "__main__":
    # h = MinHeap()
    # elems = [4, 12, 9, 4, 8, 11, 9, 13, 4]
    # # elems = [12]

    # for elem in elems:
    #     h.insert(elem)

    # print("Minheap")
    # print(h)
    # extractedElem = h.extract()
    # print(f"extracted elem {extractedElem}")
    # print("Minheap after extract")
    # print(h)

    # elems = [4, 12, 9, 4, 8, 11, 9, 13, 4]
    iterations = 1
    for _ in range(iterations):
        # elems = [random.randint(1, 1000) for _ in range(200)]
        elems = [306, 257, 291, 193, 225, 267, 151, 113, 66, 190]
        # random.shuffle(elems)
        # elems = [27, 39, 45, 34, 48, 2, 79]

        h = MaxHeap()
        h2 = MinHeap()
        for elem in elems:
            h.insert(elem)
            print(h)
            print("--------------")
            h2.insert(elem)
        h.insert(354)
        print("Maxheap")
        print(h)
        # print("Minheap")
        # print(h2)

        # extractedElem = h.extract()
        # print(f"extracted max elem {extractedElem}")
        # assert max(elems) == extractedElem

        # extractedElem = h2.extract()
        # assert min(elems) == extractedElem

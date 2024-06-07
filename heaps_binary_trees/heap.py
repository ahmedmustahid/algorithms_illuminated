from typing import Callable, List


class MinHeap:
    def __init__(self) -> None:
        self.container: List[int] = []
        self.getParentIdx: Callable[[int], int] = lambda i: i // 2

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

    def getSize(self):
        return len(self.container)

    def __getitem__(self, idx: int):
        return self.container[idx]

    def __str__(self) -> str:
        return ",".join([str(e) for e in self.container])


class MaxHeap:
    def __init__(self) -> None:
        self.container: List[int] = []
        self.getParentIdx: Callable[[int], int] = lambda i: i // 2

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

    def getSize(self):
        return len(self.container)

    def __getitem__(self, idx: int):
        return self.container[idx]

    def __str__(self) -> str:
        return ",".join([str(e) for e in self.container])


if __name__ == "__main__":
    h = MinHeap()
    elems = [4, 12, 9, 4, 8, 11, 9, 13, 4]
    # elems = [12]

    for elem in elems:
        h.insert(elem)

    print("Minheap")
    print(h)
    extractedElem = h.extract()
    print(f"extracted elem {extractedElem}")
    print("Minheap after extract")
    print(h)

    h = MaxHeap()
    elems = [4, 12, 9, 4, 8, 11, 9, 13, 4]
    # elems = [12]

    for elem in elems:
        h.insert(elem)

    print("Maxheap")
    print(h)
    extractedElem = h.extract()
    print(f"extracted elem {extractedElem}")
    print("Maxheap after extract")
    print(h)

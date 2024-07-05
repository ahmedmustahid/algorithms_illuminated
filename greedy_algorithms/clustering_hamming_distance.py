from typing import List, Dict, Tuple, Set
import itertools
from create_graph import getVerticesFromFile


def strBinToInt(x: str) -> int:
    strlist = x.split()
    s = "".join(strlist)
    b = int(s, 2)
    return b


def hammingDistance(x: str, y: str):
    xInt = strBinToInt(x)
    yInt = strBinToInt(y)

    xor = bin(xInt ^ yInt)
    xor = str(xor)

    return sum([s == "1" for s in xor])


def testHamming():
    x = "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
    y = "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1"
    print(hammingDistance(x, y))
    assert hammingDistance(x, y) == 3


def distanceFromStart(fname: str):
    strList = getVerticesFromFile(fname)
    firstnode = strList[0]
    distances = [hammingDistance(firstnode, y) for y in strList]
    return distances


def nodeToIdxsMap(fname: str) -> Dict[int, List[int]]:
    strList = getVerticesFromFile(fname)
    intList: List[int] = [strBinToInt(elem) for elem in strList]
    nodeToIdxs: Dict[int, List[int]] = {k: [] for k in intList}

    for idx, elem in enumerate(intList):
        nodeToIdxs[elem].append(idx)

    return nodeToIdxs


def getBitMasksFromCombinations(totalBits: int = 3):
    bitMasks = []
    combinationIdxs = list(itertools.combinations(range(totalBits), 2))
    for idx1, idx2 in combinationIdxs:
        singlebit = ["0"] * totalBits
        singlebit[idx1] = "1"
        singlebit[idx2] = "1"

        singlebitStr = "".join(singlebit)
        numFromBits = int(singlebitStr, 2)
        bitMasks.append(numFromBits)
    return bitMasks


def getNumsFromHummingDiff(num, hammingDist: int = 1, totalBits: int = 3) -> List[int]:
    numsHummingDiff = []
    bitMasks = []
    if hammingDist == 1:
        bitMasks = [1 << i for i in range(totalBits)]
    else:
        bitMasks = getBitMasksFromCombinations(totalBits)
    numsHummingDiff = [num ^ bitMask for bitMask in bitMasks]
    print(bitMasks)
    return numsHummingDiff


if __name__ == "__main__":
    root = "test_cases/kruskal"
    fname = "clustering_big_hamming.txt"
    fname = f"{root}/{fname}"

    x = "1 0 1 0"
    x = strBinToInt(x)

    nums = getNumsFromHummingDiff(x, hammingDist=1, totalBits=4)
    bins = [bin(num) for num in nums]
    print(*bins, sep="\n")

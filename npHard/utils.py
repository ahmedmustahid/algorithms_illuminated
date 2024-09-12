from pathlib import Path
import matplotlib.pyplot as plt
from typing import List


def getXYs(fpath):
    xs, ys = [], []

    with open(fpath, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            x, y = list(map(float, line.split()))
            xs.append(x)
            ys.append(y)
    return xs, ys

def getCoords(xs, ys):
    return list(zip(xs, ys))

def getDistances(xs,ys):
    import math
    dists = []
    xys = getCoords(xs, ys)
    xyDict = {}
    for i, xy1 in enumerate(xys):
        for j, xy2 in enumerate(xys[i+1:]):
            if (xy1,xy2) in xyDict or (xy2,xy1) in xyDict:
                continue
            dist = math.sqrt((xy1[0]- xy2[0])**2 + (xy1[1]- xy2[1])**2)
            dists.append(dist)
            xyDict[(xy1,xy2)] = dist
    return dists, xyDict, xys

globalL  = []
def createBinarySeq(m: int, l: list):
    if m==0:
        globalL.append("".join(l))
        return 
    l[m-1] = "0"
    createBinarySeq(m-1, l)
    l[m-1] = "1"
    createBinarySeq(m-1, l)

def getSubsets(xys: List[float], binarySeq: List[str]):
    m = len(xys)
    subsets = []
    for elem in binarySeq:
        elemNums = list(elem)
        subset = []
        for i, elemNum in enumerate(elemNums):
            if elemNum=="1":
                subset.append(xys[i])
        subsets.append(subset)
    return subsets



def plot(xs, ys):
    plt.scatter(xs, ys)
    plt.savefig("xvsy.png")


if __name__ == "__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fpath = root / fname

    xs, ys = getXYs(str(fpath))
    print(xs)
    print(ys)

    dists, xyDict, xys = getDistances(xs, ys)
    print(f"xys: {xys}")
    print(f"max dist: {max(dists)}")
    print(f"min dist: {min(dists)}")
    import statistics
    print(f"median {statistics.median(dists)}")
    print(f"xs len: {len(xs)}, dists len {len(dists)}, distsDict len {len(xyDict)}")
    print(getDistances([0,0,0, 1],[0,1,2, 1]))

    createBinarySeq(m=3, l=[0 for _ in range(3)])
    print(globalL)

    xys = [0,1,2]
    print(getSubsets(xys, globalL))
    

from pathlib import Path
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List, Tuple


def getXYs(fpath):
    xs, ys = [], []
    idToxy = {}
    with open(fpath, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            x, y = list(map(float, line.split()))
            xs.append(x)
            ys.append(y)
            idToxy[i] = (x,y)
    return xs, ys, idToxy

def getCoords(xs, ys):
    return list(zip(xs, ys))

def calculateDist(xy1: Tuple[int,int],xy2: Tuple[int,int]):
    import math
    dist = math.sqrt((xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2)
    return dist

def getDistances(idToxy):
    xyDict = {}
    dists = [] 
    for i, k in enumerate(idToxy.keys()):
        for _, l in enumerate(list(idToxy.keys())[i+1:]):
            if (k,l) in xyDict or (l,k) in xyDict:
                continue
            dist = calculateDist(idToxy[k],idToxy[l])
            xyDict[(k,l)] = round(dist,2)
            dists.append(dist)
    return xyDict, dists

    

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
    subsets = defaultdict(list)
    for elem in binarySeq:
        elemNums = list(elem)
        subset = set()
        for i, elemNum in enumerate(elemNums):
            if elemNum=="1":
                subset.add(xys[i])
        key = len(subset)
        subsets[key].append(subset)
    #remove subsets with length 0 or 1
    subsets.pop(0)
    subsets.pop(1)
    return subsets



def plot(xs, ys):
    fig, ax = plt.subplots()
    ax.scatter(xs, ys)

    for i, txt in enumerate(range(len(xs))):
        ax.annotate(txt+1, (xs[i], ys[i]))
    
    plt.savefig("xvsy.png")



if __name__ == "__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fpath = root / fname

    xs, ys, idToxy = getXYs(str(fpath))
    # plot(xs, ys)
    # print(xs)
    # print(ys)

    xyDict, dists = getDistances(idToxy)
    print(f"max dist: {max(dists)}")
    print(f"min dist: {min(dists)}")
    import statistics
    print(f"median {statistics.median(dists)}")
    print(f"xs len: {len(xs)}, dists len {len(dists)}, distsDict len {len(xyDict)}")
    print(getDistances({1:(0,0), 2:(0,2), 3:(0,1)}))
    # print(f"xyDict {xyDict}")
    createBinarySeq(m=3, l=[0 for _ in range(3)])
    print(globalL)

    xys = [0,1,2]
    print(getSubsets(xys, globalL))
    

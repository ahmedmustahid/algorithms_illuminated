from pathlib import Path
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict
import heapq
from typing import List, Tuple, Dict, Set, Iterable
import pprint
import sys
import itertools
from multiprocessing import Pool, cpu_count



def idxToXY(xyDict: Dict[Tuple[float,float], int]):
    idxFromXys = {v:k for k,v in xyDict.items() }
    return idxFromXys


def getXYs(fpath, t=""):
    xs, ys = [], []
    xyDict = {}
    idToxy = defaultdict(list)
    with open(fpath, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            idx, x, y = list(map(float, line.split()))
            xs.append(x)
            ys.append(y)
            # x, y = round(x,2), round(y,2)
            idToxy[x].append(y)
            # heapq.heappush(idToxy[x],y)
            xyDict[(x,y)] = idx
    if t=="small":
        idToxy2 = idToxy.copy()
        keys = sorted(list(idToxy.keys()))
        idToxy = {}
        for k in keys:
            idToxy[k] = idToxy2[k]
 
    xys = []
    for x,y in zip(xs,ys):
        xys.append((x,y))
    if t=="small":
        xys = sorted(xys,key=lambda x: x[0])
    return xys, xyDict, idToxy

def getCoords(xs, ys):
    return list(zip(xs, ys))

def calculateDist(xy1: Tuple[int,int],xy2: Tuple[int,int]):
    import math
    dist = math.sqrt((xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2)
    # dist = (xy1[0]-xy2[0])**2 + (xy1[1]-xy2[1])**2
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

def createPairsFromList(idList: List[int])->Set[Tuple[int, int]]:
    pairs = set(itertools.combinations(idList,2))
    return pairs



def getLargeDists(xyDistDict: Dict[Tuple[int, int], float], disThreshold: int):
    xyLargeDists = set(frozenset(k) for k in xyDistDict.keys() if xyDistDict[k]>=disThreshold)
    return xyLargeDists


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

def power_set(A: Iterable, xyLargeDists: Set[Tuple[int, int]]): 
    subsets = []
    N = len(A)

    total = 0 
    # iterate over each subset
    for mask in range(1<<N):
        subset = []
        for n in range(N):
            if ((mask>>n)&1) == 1:
                subset.append(A[n])
        subset = set(subset)

        if 1 not in subset:
            continue

        if len(subset)==2:
            if subset in xyLargeDists:
                # print(f"omitting {subset}")
                total += 1
                continue
        else:
            for largeelem in xyLargeDists:
                if subset.intersection(set(largeelem)):
                    # print(f"omitting {subset}")
                    total += 1
                    continue
        subsets.append(subset)
    print(f"total removed {total}")

    S = defaultdict(list) 
    for i, subset in enumerate(subsets):
        size = len(subset)
        if size==0 or size==1:
            continue
        S[size].append(subset)

    return S


def plot(xs, ys):
    fig, ax = plt.subplots()
    ax.scatter(xs, ys, s=0.05)

    # for i, txt in enumerate(range(len(xs))):
    #     ax.annotate(txt+1, (xs[i], ys[i]))
    
    plt.savefig("xvsy.png")

def totalSubsetNum(subsets):
    total = 0
    for k,v in subsets.items():
        total+= len(subsets[k])
    return total

if __name__ == "__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases/tsp_greedy"
    fname = "tsp_greedy.txt"
    fpath = root / fname

    xyDict, xToyList = getXYs(str(fpath))
    
    # print(xs)
    # print(ys)
    # print(xToyHeap)
    # pprint.pprint(xyDict)
    pprint.pprint(xToyList)
    print(len(xToyList))
    # xys = list(zip(xs,ys))

    # with Pool(cpu_count()) as p:
    #     xyDict, dists = getDistances(idToxy)
        
    # pprint.pprint(xyDict)

from utils import getXYs, getDistances, globalL, getSubsets, createBinarySeq, MinValueDict
from pathlib import Path
from typing import Tuple, Dict, List, DefaultDict, Set
import pprint
import random
DIST_THRESH=0
def deleteSmalldists(xyDict, idToxy):
    delKeys = {xy for xy in xyDict.keys() if xyDict[xy]<DIST_THRESH}

    def removeKey(key, idToxy):
        if key in idToxy:
            idToxy.pop(key)

    for delKey in delKeys:
        # print(f"delKey: {delKey}, {xyDict[delKey]}")
        removeKey(delKey[1], idToxy)
    return idToxy

def bellmanHeldKarp(xyDistDict:Dict[Tuple[int, int], float], subsets: DefaultDict[int, List[Set[int]]]):
    minNode = None
    A = MinValueDict(minNode=minNode)

    for k,v in xyDistDict.items():
        if 1 in k:
            A[k] = v
            print(f"minNode {A.minNode}")
    pprint.pprint(f"A {A}")

    maxSize = max(subsets)

    for size in range(3, maxSize+1):
        for subset in subsets[size]:
            if 1 not in subset:
                continue
            for j in subset - {1}:
                oldKey = subset - {j}
                for k in subset - {1} - {j}:
                    newKey = oldKey.union({k,j})
                    print("------------")
                    print(f"subset {subset}")
                    print(f"oldKey: {oldKey}[{k}]")
                    print(f"newKey: {newKey}[{j}]")
                    print("------------")


if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fname = "input_float_11_4.txt"
    fname = "input_float_10_4.txt"
    fpath = root / fname

    xs, ys, idToxy = getXYs(str(fpath))
    xyDistDict, dists = getDistances(idToxy)
    # pprint.pprint(f"dists {dists}")
    pprint.pprint(xyDistDict)

    idToxy = deleteSmalldists(xyDistDict, idToxy)
    m=len(idToxy)
    l = [0 for _ in range(m)]
    createBinarySeq(m, l)
    print(f"binary digits lens: {len(globalL)}")
    subsets = getSubsets(list(idToxy.keys()), globalL)
    pprint.pprint(subsets)
    print(f"xys len: {len(list(idToxy.keys()))}")
    print(f"random subset : {subsets[2][:10]}")

    bellmanHeldKarp(xyDistDict, subsets)
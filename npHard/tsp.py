from utils import getXYs, getDistances, globalL, getSubsets, createBinarySeq, MinValueDict
from pathlib import Path
from typing import Tuple, Dict, List, DefaultDict, Set
import heapq
from pprint import pformat
import logging


logging.basicConfig(filename='myapp.log',filemode="w", level=logging.DEBUG)
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
    minNodes = {frozenset(k):k for k,v in xyDistDict.items() if 1 in k}

    xyDistDict = {frozenset(k):v for k,v in xyDistDict.items()}    
    A = MinValueDict()

    for k,v in xyDistDict.items():
        if 1 in k:
            A[k] = v
    logging.debug(f"A {pformat(A)}")
    

    test = {frozenset(k):v for k,v in xyDistDict.items() if 1 in k}
    # print(minNodes)
    maxSize = max(subsets)

    for size in range(3, maxSize+1):
        for subset in subsets[size]:
            if 1 not in subset:
                continue
            h = []
            for j in subset - {1}:
                oldKey = subset - {j}
                for k in subset - {1} - {j}:
                    logging.debug("------------")
                    logging.debug(f"k:{k},j:{j}")
                    logging.debug(f"subset {subset}")
                    logging.debug(f"oldKey: {oldKey}[{k}]")
                    logging.debug(f"newKey: {subset}[{j}]")
                    startNode = minNodes[frozenset(oldKey)][1]
                    if k!=startNode:
                        continue
                    endNode = j
                    logging.debug(f"startnode:{startNode}, endNode: {endNode}")
                    if size < maxSize:
                        newval = test[frozenset(oldKey)] + xyDistDict[frozenset((startNode, endNode))]
                        logging.debug(f"newval: {test[frozenset(oldKey)]}+{xyDistDict[frozenset((startNode, endNode))]}")
                    else:
                        newval = test[frozenset(oldKey)] + xyDistDict[frozenset((startNode, endNode))] + xyDistDict[frozenset((endNode, 1))]
                        logging.debug(f"newval: {test[frozenset(oldKey)]}+{xyDistDict[frozenset((startNode, endNode))]};{xyDistDict[frozenset((endNode, 1))]}")

                    newval = round(newval,2)
                    heapq.heappush(h, (newval, (k,j)))
                    # print("------------")
            minVal, minNode = heapq.heappop(h)
            minNodes[frozenset(subset)] = minNode
            test[frozenset(subset)] = minVal


            logging.debug(f"minVal {minVal}, minNode {minNode}")
            logging.debug(f"minNodes\n{pformat(minNodes)}")
            # print("======")
            logging.debug(f"test\n{pformat(test)}")
            # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fname = "input_float_11_4.txt"
    fname = "input_float_12_4.txt"
    fname = "input_float_20_6.txt"
    fname = "input_float_10_4.txt"
    fpath = root / fname

    xs, ys, idToxy = getXYs(str(fpath))
    xyDistDict, dists = getDistances(idToxy)
    # pprint.pprint(f"dists {dists}")
    # pprint.pprint(xyDistDict)

    idToxy = deleteSmalldists(xyDistDict, idToxy)
    m=len(idToxy)
    l = [0 for _ in range(m)]
    createBinarySeq(m, l)
    # print(f"binary digits lens: {len(globalL)}")
    subsets = getSubsets(list(idToxy.keys()), globalL)
    # pprint.pprint(subsets)
    # print(f"xys len: {len(list(idToxy.keys()))}")
    # print(f"random subset : {subsets[2][:10]}")

    bellmanHeldKarp(xyDistDict, subsets)
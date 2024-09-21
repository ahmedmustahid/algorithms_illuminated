from utils import getXYs, getDistances, globalL, getSubsets, createBinarySeq, MinValueDict, power_set, getLargeDists, totalSubsetNum
from clustering import convertPointToID, getClusters, edgePointsFromClusters, getClustersOfIds
from pathlib import Path
from typing import Tuple, Dict, List, DefaultDict, Set
import heapq
import pprint
from pprint import pformat
import logging
import sys


logging.basicConfig(filename='myapp.log',filemode="w", level=logging.INFO)
DIST_THRESH_SMALL=400
def deleteSmalldists(xyDict, idToxy):
    delKeys = {xy for xy in xyDict.keys() if xyDict[xy]>DIST_THRESH_LARGE }
    # delKeys = {xy for xy in xyDict.keys() if xyDict[xy]<DIST_THRESH_SMALL }

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
        #deleting unnecessary elements
        test = {k:v for k,v in test.items() if not len(k)<size}
        minNodes = {k:v for k,v in minNodes.items() if not len(k)<size}
        logging.debug(f"test size\n{pformat(test)}")

    return test

if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "input_float_11_4.txt"
    fname = "input_float_12_4.txt"
    fname = "input_float_20_6.txt"
    fname = "input_float_10_4.txt"
    fname = "input_float_34_10.txt"
    fname = "tsp.txt"
    fname = "input_float_74_20.txt"
    fpath = root / fname

    xs, ys, idToxy = getXYs(str(fpath))
    xyDistDict, dists = getDistances(idToxy)
    print(f"len before {len(xyDistDict)}")
    print(f"len after {len(xyDistDict)}")
    pprint.pprint(xyDistDict)

    # xys = list(zip(xs,ys))
    # clusters = getClusters(points=xys,n_clusters=2)
    # idclusters = getClustersOfIds(clustersDict=clusters, idToxy=idToxy)
    # pprint.pprint(idclusters)


    allPairs = set()

    for ks in xyDistDict.keys():
        for k in ks:
            allPairs.add(k)

    DIST_THRESH_LARGE=12
    xyLargeDistDict = getLargeDists(xyDistDict, disThreshold=DIST_THRESH_LARGE)

    subsets = power_set(list(allPairs), xyLargeDistDict)
    print(f"random subset : {subsets[2][:10]}")
    print(f"total subset num {totalSubsetNum(subsets)}")

    test = bellmanHeldKarp(xyDistDict, subsets)
    print(test)
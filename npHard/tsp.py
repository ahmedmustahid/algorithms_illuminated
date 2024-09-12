from utils import getXYs, getDistances, globalL, getSubsets, createBinarySeq
from pathlib import Path
import pprint

def deleteSmalldists(xyDict, idToxy):
    delKeys = {xy for xy in xyDict.keys() if xyDict[xy]<400}

    def removeKey(key, idToxy):
        if key in idToxy:
            idToxy.pop(key)

    for delKey in delKeys:
        removeKey(delKey[1], idToxy)
    return idToxy

if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fpath = root / fname

    xs, ys, idToxy = getXYs(str(fpath))
    xyDict, dists = getDistances(idToxy)
    # pprint.pprint(xyDict)

    idToxy = deleteSmalldists(xyDict, idToxy)
    m=len(idToxy)
    l = [0 for _ in range(m)]
    createBinarySeq(m, l)
    print(len(globalL))
    subsets = getSubsets(list(idToxy.keys()), globalL)

    print(f"xys len: {len(list(idToxy.keys()))}")
    print(len(subsets))
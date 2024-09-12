from utils import getXYs, getDistances, globalL, getSubsets, createBinarySeq
from pathlib import Path


if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases"
    fname = "tsp.txt"
    fpath = root / fname

    xs, ys = getXYs(str(fpath))
    dists, xyDict, xys = getDistances(xs, ys)

    m=len(xys)
    l = [0 for _ in range(m)]
    createBinarySeq(m, l)
    print(globalL)
    # subsets = getSubsets(xys, globalL)

    # print(f"xys len: {len(xys)}")
    # print(len(subsets))
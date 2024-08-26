from typing import Dict
import heapq
from collections import defaultdict


def getGraph(fname: str) -> defaultdict[str, Dict[str, int]]:
    d: defaultdict[str, Dict[str, int]] = defaultdict(dict)

    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            head, tail, cost = line.split()
            d[head][tail] = int(cost)
    return d


def createGraph(fileName):
    graph = defaultdict(lambda: {"children": {}, "length": float("inf")})
    children = set()
    with open(fileName) as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            head, tail, cost = line.split()
            graph[head]["children"][tail] = int(cost)
            children.add(tail)
    print()
    noChildNodes = children - set(graph.keys())
    if noChildNodes:
        for nc in noChildNodes:
            graph[nc]["children"] = {}
    return graph


def getChildrenIDx(parentIdx: int, maxLen: int):
    c1idx, c2idx = 2 * parentIdx + 1, 2 * parentIdx + 2
    if c2idx > (maxLen - 1):
        if c1idx > (maxLen - 1):
            return None
        else:
            return c1idx, None

    return c1idx, c2idx


def heapqDelete(H, idx):
    # H[idx], H[-1] = H[-1], H[idx]
    H[idx] = H[-1]
    H.pop()
    # heapq.heapify(H) #O(n)
    if idx < len(H):
        heapq._siftup(H, idx)
        heapq._siftdown(H, 0, idx)
    return H


def getIdx(H, child):
    for i, elem in enumerate(H):
        k, c = elem
        if child == c:
            return k, i
    return None


if __name__ == "__main__":
    fname = "test_cases/dijkstraSmall.txt"
    graph = createGraph(fname)
    graph["1"]["length"] = 0

    X = set()
    l = []
    H = []
    for node in graph.keys():
        key = graph[node]["length"]
        H.append((key, node))
    heapq.heapify(H)
    print(H)
    while H:
        cost, node = heapq.heappop(H)
        X.add(node)
        l.append(node)

        for c in graph[node]["children"].keys():
            k, idx = getIdx(H, c)
            H = heapqDelete(H, idx)
            print(H)
            lnc = cost + graph[node]["children"][c]
            k = min(k, lnc)
            heapq.heappush(H, (k, c))

            print(H)
    print(l)

from typing import Dict
import heapq
from pathlib import Path
import networkx as nx
from collections import defaultdict


def createGraph1(fileName):
    graph = defaultdict(lambda: {"children": {}, "length": float("inf")})
    with open(fileName) as f:
        for line in f:
            test = line.split()
            for child in test[1:]:
                node, weight = map(int, child.split(","))
                graph[test[0]]["children"][str(node)] = weight
    # pp.pprint(graph)
    # sys.exit()
    return graph


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
    # print()
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


def createNetworkx(graph, tails):
    G = nx.DiGraph()
    # graph = createGraph(fileName)

    for head in graph:
        for tail, weight in graph[head]["children"].items():
            G.add_edge(head, tail, weight=weight)
    dijkstraLens = []
    for tail in tails:
        distance, _ = nx.single_source_dijkstra(G, source="1", target=tail)
        dijkstraLens.append(distance)
    return dijkstraLens


def reconstruction(prev, target):
    path = [target]
    while target != "1":
        target = prev[target]
        path.append(target)
    path.reverse()
    return path


def dijkstra(graph, source="1", target=None):
    # graph = createGraph1(fileName)

    graph[source]["length"] = 0

    X = set()
    path = []
    mins = {source: 0}

    prev = {}
    H = []
    for node in graph.keys():
        cost = graph[node]["length"]
        H.append((cost, node))
    heapq.heapify(H)

    while H:
        cost, node = heapq.heappop(H)
        X.add(node)
        mins[node] = cost
        if target and node == target:
            # path = reconstruction(prev, target)
            return path, mins

        for c in graph[node]["children"].keys():
            if c in X:
                continue
            k, idx = getIdx(H, c)
            H = heapqDelete(H, idx)
            lnc = cost + graph[node]["children"][c]
            k = min(k, lnc)
            prev[c] = node
            heapq.heappush(H, (k, c))

    return path, mins


if __name__ == "__main__":
    # fileName = Path.home()/"work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/dijkstraChallenge.txt"
    fileName = (
        Path.home()
        / "work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/testCase1.txt"
    )
    fileName = (
        Path.home()
        / "work/algorithms_illuminated/graph_algorithm/Dijkstra/testCases/dijkstraChallenge.txt"
    )
    graph = createGraph1(fileName)
    nodelist = "1,2,3,4,5,6,7,8".split(",")
    nodelist = "7,37,59,82,99,115,133,165,188,197".split(",")

    costs = []
    for node in nodelist:
        _, c = dijkstra(fileName=fileName, target=node)
        # costs.append(c)
        # print(f"node {node}, path:{p}, cost:{c}")
    for node in nodelist:
        costs.append(str(c[node]))
    print(",".join(costs))
    # p, c = dijkstra(fileName=fileName)
    # print(f"node {node}, path:{p}, cost:{c}")
    graph = createGraph1(fileName)
    print(createNetworkx(graph, tails=nodelist))

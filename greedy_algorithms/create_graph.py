from collections import defaultdict
from typing import List, Dict, Tuple, Set

import networkx as nx


def getGraph(fname: str):
    graph: List[Tuple[str, str, int]] = []
    graphDict: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    with open(fname, "r") as f:
        for line in f:
            if len(line.split()) < 3:
                continue
            v1, v2, weight = line.split()
            weight = int(weight)
            temp = (v1, v2, weight)
            graph.append(temp)

    for v1, v2, weight in graph:
        graphDict[v1].append((v2, weight))
        graphDict[v2].append((v1, weight))

    return graphDict


def getEdges(fname: str):
    edges: List[Tuple[str, str, int]] = []
    with open(fname, "r") as f:
        for line in f:
            if len(line.split()) < 3:
                continue
            v1, v2, weight = line.split()
            weight = int(weight)
            temp = (v1, v2, weight)
            edges.append(temp)

    return edges


def getVertices(edges: List[Tuple[str, str, int]]) -> Set:
    vertices: List[str] = []
    for edge in edges:
        v, w, _ = edge
        vertices.append(v)
        vertices.append(w)
    return set(vertices)


def getNxGraph(fname: str):
    graph: List[Tuple[str, str, Dict[str, int]]] = []
    with open(fname, "r") as f:
        for line in f:
            if len(line.split()) < 3:
                continue
            v1, v2, weight = line.split()
            weight = int(weight)
            temp = (v1, v2, {"weight": weight})
            graph.append(temp)

    G = nx.Graph()
    for g in graph:
        e1, e2, wt = g
        G.add_edge(e1, e2, weight=wt["weight"])

    return G


if __name__ == "__main__":
    testDir = "test_cases/prob3"
    fname = f"{testDir}/pg59.txt"
    fname = f"{testDir}/input_random_33_1000.txt"
    fname = f"{testDir}/challenge_case.txt"

    # print(getGraph(fname))
    G = getNxGraph(fname)
    G = nx.minimum_spanning_tree(G)
    s = sorted(G.edges(data=True))
    mincost = sum(
        [e[2]["weight"] for e in s]
    )  # [('1', '2', {'weight': 1}), ('1', '3', {'weight': 4}), ('2', '4', {'weight': 2})]
    print(s)
    print(f"mincost {mincost}")

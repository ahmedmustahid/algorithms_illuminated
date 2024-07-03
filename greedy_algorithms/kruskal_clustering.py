from typing import List, Dict, Tuple, Set
from union_find import UnionFind
from create_graph import getEdges, getVertices


def getRoots(U: Dict[str, UnionFind], T: Dict[Tuple[str, str], int]):
    rootDict = {}
    for k, v in T.items():
        e, _ = k
        ue = U[e]
        root = UnionFind.find(ue)
        rootDict[k] = root
    return rootDict


def kruskal_clustering(edges: List[Tuple[str, str, int]], k: int = 4):
    # T: Set[Tuple[str, str]] = set()
    T: Dict[Tuple[str, str], int] = {}
    # parents: Set[str] = set()
    edges = getEdges(fname)
    vertices = getVertices(edges)
    n = len(vertices)
    U: Dict[str, UnionFind] = UnionFind.initialize(vertices)

    edges = sorted(edges, key=lambda x: x[2])

    minCosts = 0
    costs = []
    totalUnion = 0
    for edge in edges:
        v, w, cost = edge
        uv, uw = U[v], U[w]
        if UnionFind.find(uv) != UnionFind.find(uw):
            if totalUnion == n - k:
                return cost
            T[(v, w)] = cost

            UnionFind.union(U, uv, uw)
            costs.append(cost)
            minCosts += cost
            totalUnion += 1

    return cost


if __name__ == "__main__":
    root = "test_cases/kruskal"
    # root = "test_cases/prob3"
    # fname = "challenge_case.txt"
    fname = "simple2.txt"
    fname = "input_completeRandom_18_128.txt"
    # fname = "input_completeRandom_1_8.txt"
    # fname = "input_completeRandom_10_32.txt"
    # fname = "simple.txt"
    fname = "clustering1.txt"
    fname = "input_completeRandom_30_1024.txt"
    fname = f"{root}/{fname}"

    edges = getEdges(fname)
    c = kruskal_clustering(edges, k=4)

    print(c, sep="\n")
    # print(len(T))

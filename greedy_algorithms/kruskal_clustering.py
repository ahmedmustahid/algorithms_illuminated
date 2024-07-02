from typing import List, Dict, Tuple, Set
from union_find import UnionFind
from create_graph import getEdges, getVertices


def kruskal_clustering(edges: List[Tuple[str, str, int]]):
    T: Set[Tuple[str, str]] = set()

    edges = getEdges(fname)
    vertices = getVertices(edges)
    U: Dict[str, UnionFind] = UnionFind.initialize(vertices)

    edges = sorted(edges, key=lambda x: x[2])

    minCosts = 0
    for edge in edges:
        v, w, cost = edge
        uv, uw = U[v], U[w]

        if UnionFind.find(uv) != UnionFind.find(uw):
            if (v, w) not in T or (w, v) not in T:
                T.add((v, w))
            UnionFind.union(U, uv, uw)
            minCosts += cost

    return T, minCosts


if __name__ == "__main__":
    root = "test_cases/kruskal"
    fname = "clustering1.txt"
    root = "test_cases/prob3"
    fname = "challenge_case.txt"
    fname = f"{root}/{fname}"

    edges = getEdges(fname)
    _, m = kruskal_clustering(edges)

    # print(*T, sep="\n")
    print(m)

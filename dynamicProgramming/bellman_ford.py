from typing import Dict
from pathlib import Path
from collections import defaultdict


def createBFGraph(fname):
    graph = defaultdict(lambda: {"heads": {}, "inDegree": 0, "length": float("inf")})
    heads = []
    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            head, tail, cost = line.split()
            heads.append(head)
            graph[tail]["heads"][head] = int(cost)
    for tail in graph.keys():
        graph[tail]["inDegree"] = len(graph[tail]["heads"])
    for head in heads:
        if not head in graph:
            graph[head]["heads"] = {}
            graph[head]["inDegree"] = 0
            graph[head]["length"] = float("inf")
    return graph


def calcMinEdge(graph, tail, prev, i):
    for j, head in enumerate(graph[tail]["heads"]):
        if j > i:
            break
        lht = graph[tail][]


def BellmanFord(fname):
    graph = createBFGraph(str(p))
    print(graph)

    curr = {tail: float("inf") for tail in graph.keys()}
    prev = {tail: float("inf") for tail in graph.keys()}

    graph["1"]["length"] = 0
    prev["1"] = 0

    n = len(graph)
    for i in range(n + 1):
        stable = True
        for tail in graph:
            if not i <= graph[tail]["inDegree"]:
                curr = min(
                    prev[tail],
                )
            else:
                curr[tail] = prev[tail]


if __name__ == "__main__":
    p = Path.cwd() / "test_cases/bellmanFord/"
    fname = "small.txt"
    p = p / fname
    BellmanFord(str(p))

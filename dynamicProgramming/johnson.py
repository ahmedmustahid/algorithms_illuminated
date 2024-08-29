from bellman_ford import createBFGraph, BellmanFord
from dijkstra import getGraph, dijkstra
from pathlib import Path


def addDummySource(BFGraph):
    for tail in BFGraph:
        BFGraph[tail]["heads"]["s"] = 0
        BFGraph[tail]["inDegree"] += 1
    BFGraph["s"]["heads"] = {}
    BFGraph["s"]["inDegree"] = 0
    BFGraph["s"]["length"] = 0
    return BFGraph


def johnson(fname):
    BFGraph = createBFGraph(fname)
    dijGraph = getGraph(fname)

    BFGraphDummy = addDummySource(BFGraph)
    BFcosts = BellmanFord(BFGraphDummy, source="s")
    return BFcosts


if __name__ == "__main__":
    p = Path.cwd() / "test_cases/bellmanFord/"
    fname = "johnsonSmall.txt"
    source = "1"
    # fname = "small2.txt"
    # source = "a"
    # fname = "negcycle1.txt"
    # source = "a"
    p = p / fname

    costs = johnson(str(p))
    print(costs)

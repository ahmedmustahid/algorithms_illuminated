from bellman_ford import createBFGraph, BellmanFord
from dijkstra import getGraph, dijkstra
from collections import defaultdict
from pathlib import Path


def addDummySource(BFGraph):
    for tail in BFGraph:
        BFGraph[tail]["heads"]["s"] = 0
        BFGraph[tail]["inDegree"] += 1
    BFGraph["s"]["heads"] = {}
    BFGraph["s"]["inDegree"] = 0
    BFGraph["s"]["length"] = 0
    return BFGraph


def addBFCostsToGraph(BFGraphDummy, BFCosts):
    for tail in BFGraphDummy:
        BFGraphDummy[tail]["length"] = BFCosts[tail]
    return BFGraphDummy


def convertToDijkstraGraph(BFGraph):
    dijGraph = defaultdict(lambda: {"children": {}, "length": float("inf")})
    for tail in BFGraph:
        for head in BFGraph[tail]["heads"]:
            dijGraph[head]["children"][tail] = BFGraph[tail]["heads"][head]

    return dijGraph


def reweight(BFGraphDummy, BFCosts):
    offsetForEachVertex = {}
    BFGraphDummy = addBFCostsToGraph(BFGraphDummy, BFCosts)
    BFGraphDummy.pop("s")
    for tail in BFGraphDummy:
        BFGraphDummy[tail]["heads"].pop("s")
        lengthTail = BFGraphDummy[tail]["length"]
        for head in BFGraphDummy[tail]["heads"]:
            lengthHead = BFGraphDummy[head]["length"]
            offset = lengthHead - lengthTail
            reweightedCost = BFGraphDummy[tail]["heads"][head] + offset
            offsetForEachVertex[head] = offset
            BFGraphDummy[tail]["heads"][head] = reweightedCost

    # for tail in BFGraphDummy:
    #     BFGraphDummy[tail]["length"] = float("inf")
    return BFGraphDummy, offsetForEachVertex


def processAfterDij(dijCostsUnprocessed, offsetForEachVertex):
    costs = {}
    for node in dijCostsUnprocessed:
        costs[node] = dijCostsUnprocessed[node] - offsetForEachVertex[node]
    return costs


def johnson(fname, source="1"):
    dijGraph = getGraph(fname)
    BFGraph = createBFGraph(fname)

    BFGraphDummy = addDummySource(BFGraph)
    BFcosts = BellmanFord(BFGraphDummy, source="s")
    print(f"BFcosts: {BFcosts}")
    if BFcosts == "negative cycle":
        return "negative cycle"
    BFGraphReweighted, offsetForEachVertex = reweight(BFGraphDummy, BFcosts)
    print(BFGraphReweighted)

    dijGraph = convertToDijkstraGraph(BFGraphReweighted)
    print(dijGraph)

    dijCosts = []
    for node in BFGraph:
        _, dijCostsUnprocessed = dijkstra(dijGraph, source, target=node)
        dijCosts = processAfterDij(dijCostsUnprocessed, offsetForEachVertex)
        print(dijCosts)
        break
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
    source = "a"
    costs = johnson(str(p), source)

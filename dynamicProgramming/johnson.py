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
            # if head not in tails:
            #     dijGraph[head]["children"] = {}
            #     dijGraph[head]["length"] = float("inf")

    keys = set(dijGraph.keys())
    for k in keys:
        for child in dijGraph[k]["children"]:
            if not child in keys:
                dijGraph[child]["children"] = {}
                dijGraph[child]["length"] = float("inf")
    return dijGraph


def reweight(BFGraphDummy, BFCosts):
    offsetForEachVertex = {}
    BFGraphDummy = addBFCostsToGraph(BFGraphDummy, BFCosts)
    BFGraphDummy.pop("s")

    for tail in BFGraphDummy:
        BFGraphDummy[tail]["heads"].pop("s")
        lengthTail = BFGraphDummy[tail]["length"]
        offsetForEachVertex[tail] = lengthTail
        for head in BFGraphDummy[tail]["heads"]:
            lengthHead = BFGraphDummy[head]["length"]
            offset = lengthHead - lengthTail
            reweightedCost = BFGraphDummy[tail]["heads"][head] + offset
            offsetForEachVertex[head] = lengthHead
            BFGraphDummy[tail]["heads"][head] = reweightedCost
    print(f"offsets {offsetForEachVertex}")
    # for tail in BFGraphDummy:
    #     BFGraphDummy[tail]["length"] = float("inf")
    return BFGraphDummy, offsetForEachVertex


def processAfterDij(source, dijCostsUnprocessed, offsetForEachVertex):
    costs = {}
    for node in dijCostsUnprocessed:
        if source != node:
            # print(f"source: {source} node: {node}")
            costs[node] = (
                dijCostsUnprocessed[node]
                - offsetForEachVertex[source]
                + offsetForEachVertex[node]
            )
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
    print(f"BFGraphReweighted {BFGraphReweighted}")

    print()
    print()
    print()
    dijGraph = convertToDijkstraGraph(BFGraphReweighted)
    print(f"dijGraph: {dijGraph}")
    print()

    costs = []
    source = "b"
    for source in BFGraph:
        for node in BFGraph:
            if node == source:
                continue
            _, dijCostsUnprocessed = dijkstra(dijGraph, source=source, target=node)
            # print(dijCostsUnprocessed)
            dijCosts = processAfterDij(source, dijCostsUnprocessed, offsetForEachVertex)
        costs.append((source, dijCosts))
    return costs


if __name__ == "__main__":
    p = (
        Path.home()
        / "work/algorithms_illuminated/dynamicProgramming/test_cases/bellmanFord/"
    )
    fname = "johnsonSmall.txt"
    source = "1"
    # fname = "small2.txt"
    # source = "a"
    # fname = "negcycle1.txt"
    # source = "a"
    p = p / fname
    source = "a"
    costs = johnson(str(p), source)
    print(costs)

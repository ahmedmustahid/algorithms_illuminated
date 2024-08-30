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

    # exchanging tail with head and vice versa
    for tail in BFGraph:
        for head in BFGraph[tail]["heads"]:
            dijGraph[head]["children"][tail] = BFGraph[tail]["heads"][head]

    # nodes which have no children ie which were not tails
    keys = set(dijGraph.keys())
    for k in keys:
        for child in dijGraph[k]["children"]:
            if not child in keys:
                dijGraph[child]["children"] = {}
                dijGraph[child]["length"] = float("inf")

    # setting inf as default dijkstra score
    for k in dijGraph.keys():
        dijGraph[k]["length"] = float("inf")

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
    # print(f"offsets {offsetForEachVertex}")
    return BFGraphDummy, offsetForEachVertex


def processAfterDij(source, dijCostsUnprocessed, offsetForEachVertex):
    costs = {}
    for node in dijCostsUnprocessed:
        if source != node:
            costs[node] = (
                dijCostsUnprocessed[node]
                - offsetForEachVertex[source]
                + offsetForEachVertex[node]
            )
    return costs


def convertLensToInf(graph):
    for k in graph:
        graph[k]["length"] = float("inf")
    return graph


def johnson(fname, source="1"):
    dijGraph = getGraph(fname)
    BFGraph = createBFGraph(fname)
    # print(f"bfgraph {BFGraph}")

    BFGraphDummy = addDummySource(BFGraph)
    BFcosts = BellmanFord(BFGraphDummy, source="s")
    # print(f"BFcosts: {BFcosts}")
    if BFcosts == "negative cycle":
        return "negative cycle"
    BFGraphReweighted, offsetForEachVertex = reweight(BFGraphDummy, BFcosts)
    # print(f"BFGraphReweighted {BFGraphReweighted}")

    print()
    print()
    print()
    dijGraph = convertToDijkstraGraph(BFGraphReweighted)
    print()

    costs = []
    # source = "b"
    for source in BFGraph:
        # for node in BFGraph:
        #     if node == source:
        #         continue
        # print(f"dijGraph: {dijGraph}")
        _, dijCostsUnprocessed = dijkstra(dijGraph, source=source)
        # print(dijCostsUnprocessed)
        dijCosts = processAfterDij(source, dijCostsUnprocessed, offsetForEachVertex)
        dijGraph = convertLensToInf(dijGraph)
        costs.append((source, dijCosts))
    return costs


if __name__ == "__main__":
    p = Path.home() / "work/algorithms_illuminated/dynamicProgramming/test_cases/apsp/"

    # fname = "johnsonSmall.txt"
    # source = "1"
    def getMin(tupleCosts):
        mindicts = []
        minvals = []
        for t in tupleCosts:
            source = t[0]
            t1 = t[1]
            k = min(t1, key=t1.get)
            v = t1[k]
            minvals.append(v)
            mindicts.append({"source": source, "min": (k, v)})

        mincost = min(minvals)

        return mincost

    fname = "input_random_24_64.txt"
    fname = "input_random_26_128.txt"
    fname = "input_random_35_512.txt"

    p = p / fname
    source = "a"
    costs = johnson(str(p), source)
    if not isinstance(costs, list):
        print(costs)
    else:
        minCost = getMin(costs)
        print(f"mincost: {minCost}")

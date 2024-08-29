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
    costs = [float("inf")]
    cost = float("inf")
    for j, head in enumerate(graph[tail]["heads"]):
        # if j > i:
        #     break
        cost = prev[head] + graph[tail]["heads"][head]
        costs.append(cost)
    return min(costs)


def BellmanFord(fname, source="1"):
    graph = createBFGraph(str(p))
    print(graph)

    curr = {tail: float("inf") for tail in graph.keys()}
    prev = {tail: float("inf") for tail in graph.keys()}

    graph[source]["length"] = 0
    prev[source] = 0
    curr[source] = 0

    n = len(graph)
    for i in range(1, n + 1):
        stable = True
        for tail in graph:
            if not graph[tail]["inDegree"] > 0:
                continue
            if i <= graph[tail]["inDegree"]:
                curr[tail] = min(prev[tail], calcMinEdge(graph, tail, prev, i))
            else:
                curr[tail] = prev[tail]

            if curr[tail] != prev[tail]:
                stable = False

            prev = curr.copy()

        if stable == True:
            return curr
    return "negative cycle"


if __name__ == "__main__":
    p = Path.cwd() / "test_cases/bellmanFord/"
    fname = "small.txt"
    source = "1"
    fname = "small2.txt"
    source = "a"
    fname = "negcycle1.txt"
    source = "a"
    p = p / fname
    c = BellmanFord(str(p), source)
    print(c)

from collections import defaultdict
from pathlib import Path
from bellman_ford import createBFGraph, BellmanFord
from johnson import addDummySource, reweight


def minApsp(BFGraph):
    BFGraphDummy = addDummySource(BFGraph)
    BFcosts = BellmanFord(BFGraphDummy, source="s")
    if BFcosts == "negative cycle":
        return "negative cycle"
    BFGraphReweighted, _ = reweight(BFGraphDummy, BFcosts)

    return BFGraphReweighted


def getMinLen(BFGraphReweighted):
    lens = []

    for node in BFGraphReweighted.keys():
        lens.append(BFGraphReweighted[node]["length"])

    return min(lens)


if __name__ == "__main__":
    p = Path.home() / "work/algorithms_illuminated/dynamicProgramming/test_cases/apsp/"
    fname = "input_random_24_64.txt"
    fname = "input_random_30_256.txt"
    fname = "input_random_26_128.txt"
    fname = "input_random_35_512.txt"
    # fname = "g3.txt"
    # fname = "input_random_44_2048.txt"

    p = p / fname
    source = "a"

    BFGraph = createBFGraph(str(p))
    # print(BFGraph)
    b = minApsp(BFGraph)
    if not isinstance(b, str):
        ml = getMinLen(b)
        print(ml)
    else:
        print(b)

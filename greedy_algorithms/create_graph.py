from collections import defaultdict
from typing import List, Dict, Tuple


def getGraph(fname: str):
    graph: List[Tuple[str, Tuple[str, int]]] = []
    graphDict: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            v1, v2, weight = line.split()
            weight = int(weight)
            temp = (v1, (v2, weight))
            graph.append(temp)

    for key, value in graph:
        graphDict[key].append(value)

    return graphDict


if __name__ == "__main__":
    testDir = "test_cases/prob3"
    fname = f"{testDir}/edges_prob3.txt"

    print(getGraph(fname))

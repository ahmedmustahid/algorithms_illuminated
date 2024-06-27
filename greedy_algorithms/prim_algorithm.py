from create_graph import getGraph
from queue import Queue
from collections import defaultdict
from typing import List, Dict, Tuple, Set

if __name__ == "__main__":
    testDir = "test_cases/prob3"
    fname = f"{testDir}/input_random_10_40.txt"
    fname = f"{testDir}/input_random_33_1000.txt"
    fname = f"{testDir}/challenge_case.txt"
    # fname = f"{testDir}/pg59.txt"

    graphDict: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
    graphDict = getGraph(fname)
    print(graphDict)
    print("-----------------------------------------")

    key = list(graphDict.keys())[0]
    X: Set[str] = {key}
    q: Queue[str] = Queue()
    q.put(key)
    candidates: Dict[Tuple[str, str], int] = {}
    T: List[Tuple[str, str]] = []

    minCostSum = 0

    while not q.empty():
        key = q.get()
        for node, cost in graphDict[key]:
            if node not in X:
                candidates[(key, node)] = cost

        candidatesCopy = candidates.copy()
        for k, _ in candidatesCopy.items():
            n1, n2 = k
            if n1 in X and n2 in X:
                candidates.pop(k)

        if candidates:
            minedge = min(candidates.items(), key=lambda x: x[1])
            minNode = minedge[0][1]
            X.add(minNode)
            q.put(minNode)
            T.append(minedge[0])
            minCostSum += candidates[minedge[0]]
            candidates.pop(minedge[0])

        print(candidates)
        print(X)
        print(T)
        print(minCostSum)
        print("---------------------------------------")

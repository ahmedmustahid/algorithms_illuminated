from create_graph import getGraph
from queue import Queue
from collections import defaultdict
from typing import List, Dict, Tuple, Set

if __name__ == "__main__":
    testDir = "test_cases/prob3"
    fname = f"{testDir}/input_random_10_40.txt"

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
        for value in graphDict[key]:
            node = value[0]
            cost = value[1]
            if node not in X:
                temp_key1 = (key, node)
                temp_key2 = (node, key)
                if temp_key1 not in candidates or temp_key2 not in candidates:
                    candidates[(key, value[0])] = value[1]
        print(candidates)
        minNode: Tuple[str, str] = min(candidates, key=candidates.get)  # type: ignore
        print(minNode)  # type: ignore
        X.add(minNode[1])  # type: ignore
        minCostSum += candidates[minNode]
        print(minCostSum)
        candidates.pop(minNode)  # type: ignore

        T.append(minNode)  # type: ignore
        print(T)

        q.put(minNode[1])  # type: ignore

    # for key, values in graphDict.items():
    #     if key in X:
    #         for value in values:
    #             if value[0] not in X:
    #                 temp_key1 = (key, value[0])
    #                 temp_key2 = (value[0], key)
    #                 if temp_key1 not in candidates or temp_key2 not in candidates:
    #                     candidates[(key, value[0])] = value[1]
    #         print(candidates)
    #         minNode: Tuple[str, str] = min(candidates, key=candidates.get)  # type: ignore
    #         print(minNode)  # type: ignore
    #         X.add(minNode[1])  # type: ignore
    #         minCostSum += candidates[minNode]
    #         print(minCostSum)
    #         candidates.pop(minNode)  # type: ignore

    #         T.append(minNode)  # type: ignore
    #         print(T)

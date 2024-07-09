from typing import List, Tuple, Set
import sys

sys.setrecursionlimit(10000)


def getValuesAndWeights(fname: str) -> Tuple[List[int], List[int], int]:
    weights = [0]
    values = [0]
    knapsack_size = 0
    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                knapsack_size, _ = list(map(int, line.split()))
                continue
            value, size = list(map(int, line.split()))
            weights.append(size)
            values.append(value)
    return values, weights, knapsack_size


# def ka_recursive(i: int, j: int, values: List[int], weights: List[int]):
#     if i == 0:
#         return 0
#     s = weights[i]
#     v = values[i]
#     if s > j:
#         a = ka_recursive(i - 1, j, values, weights)
#         return a
#     else:
#         b = max(
#             ka_recursive(i - 1, j, values, weights),
#             ka_recursive(i - 1, j - s, values, weights) + v,
#         )
#         return b


def knapsack(fname: str):
    values, weights, knapsack_size = getValuesAndWeights(fname)
    n = len(values) - 1
    C = knapsack_size
    A = [[0 for _ in range(C + 1)] for _ in range(n)]
    S = dict()
    T = dict()
    L = []

    def ka_recursive(i: int, j: int):
        if i == 0:
            S[0, j] = 0
            return 0
        s = weights[i]
        v = values[i]
        if i == 1:
            if s > j:
                S[i, j] = 0
                return 0
            else:
                S[i, j] = v
                return v
        if (i, j) in S:
            return S[(i, j)]
        if s > j:
            a = ka_recursive(i - 1, j)
            return a
        else:
            b = max(
                ka_recursive(i - 1, j),
                ka_recursive(i - 1, j - s) + v,
            )
            S[(i, j)] = b
            return b

    a = ka_recursive(n, C)
    return a


if __name__ == "__main__":
    root = "test_cases/knapsack"
    fname = "input_random_10_100_10.txt"
    fname = "input_random_21_1000_100.txt"
    # fname = "input_random_30_10000_1000.txt"
    # fname = "small.txt"
    fname = "knapsack_big.txt"
    fname = f"{root}/{fname}"
    a = knapsack(fname)
    print(a)

    # values, weights, knapsack_size = getValuesAndWeights(fname)
    # n = len(values) - 1
    # C = knapsack_size
    # a = ka_recursive(n, C, values, weights)

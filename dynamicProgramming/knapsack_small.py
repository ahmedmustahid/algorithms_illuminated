from typing import List, Tuple, Set
# import pprint


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


def knapsackAlgorithm(fname: str) -> Tuple[Set[int], int]:
    def getKnapsackArray(
        fname: str,
    ) -> Tuple[List[List[int]], List[int], List[int], int]:
        values, weights, C = getValuesAndWeights(fname)

        n = len(values)
        A = [[0 for _ in range(C + 1)] for _ in range(n)]

        for i in range(1, n):
            for c in range(C + 1):
                if weights[i] > c:
                    A[i][c] = A[i - 1][c]
                else:
                    A[i][c] = max(A[i - 1][c], A[i - 1][c - weights[i]] + values[i])

        return A, values, weights, C

    A, values, weights, C = getKnapsackArray(fname)
    S: Set[int] = set()
    n: int = len(values)
    c = C

    for i in range(n - 1, 1, -1):
        if weights[i] <= c and A[i - 1][c - weights[i]] + values[i] >= A[i - 1][c]:
            S.add(i)
            c = c - weights[i]
    sum = 0
    for k in S:
        sum += values[k]
    return S, sum


if __name__ == "__main__":
    root = "test_cases/knapsack"
    fname = "input_random_10_100_10.txt"
    # fname = "small.txt"
    fname = "input_random_30_10000_1000.txt"
    fname = "knapsack1.txt"
    fname = f"{root}/{fname}"

    S, sum = knapsackAlgorithm(fname)
    # pprint.pprint(S)
    print(sum)

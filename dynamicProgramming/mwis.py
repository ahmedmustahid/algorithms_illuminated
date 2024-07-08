from typing import List, Set


def getWeights(fname: str) -> List[int]:
    weights = [0]

    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            weights.append(int(line))
    return weights


def getMaxIWeights(weights: List[int]):
    n = len(weights)
    A = list((0 for _ in range(n)))
    A[0], A[1] = 0, weights[1]
    for i in range(2, n):
        A[i] = max(A[i - 1], A[i - 2] + weights[i])
    return A


def getMWISNodes(maxWeights: List[int], weights: List[int]) -> Set[int]:
    S: Set[int] = set()
    i = len(maxWeights) - 1

    while i >= 2:
        if maxWeights[i - 1] >= maxWeights[i - 2] + weights[i]:
            i = i - 1
        else:
            S.add(i)
            i = i - 2
    if i == 1:
        S.add(i)

    return S


def mwis(fname: str):
    weights = getWeights(fname)
    A = getMaxIWeights(weights)
    S = getMWISNodes(A, weights)
    return S


def bitsFromStr(S: Set[int], st: str):
    arr = st.split(",")
    arr = list(map(int, arr))

    temp = ""
    for e in arr:
        if e in S:
            temp += "1"
        else:
            temp += "0"
    return temp


if __name__ == "__main__":
    root = "test_cases"
    st = "1,2,3,4,17,117,517,997"
    fname = "input_random_29_1000.txt"
    fname = "input_random_43_8000.txt"
    fname = "input_random_48_10000.txt"
    fname = "mwis.txt"
    fname = f"{root}/{fname}"

    S = mwis(fname)
    print(f"filename: {fname}")
    print(bitsFromStr(S, st))

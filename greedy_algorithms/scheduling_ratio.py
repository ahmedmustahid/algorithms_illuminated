from collections import defaultdict
from typing import Dict, List, Tuple


def merge(
    c: List[Tuple[float, float, int]], d: List[Tuple[float, float, int]]
) -> List[Tuple[float, float, int]]:
    b: List[Tuple[float, float, int]] = []
    m = len(c) + len(d)
    i, j = 0, 0

    eps = 10**-4
    for _ in range(m):
        if c[i][0] > d[j][0]:
            b.append(c[i])
            i += 1
        elif abs(c[i][0] - d[j][0]) < eps:
            # higher weight will be first
            if c[i][1] > d[j][1]:
                b.append(c[i])
                i += 1
            else:
                b.append(d[j])
                j += 1
        else:
            b.append(d[j])
            j += 1

        if i == len(c):
            return b + d[j:]

        if j == len(d):
            return b + c[i:]
    return b


def mergeSort(arr: List[Tuple[float, float, int]]) -> List[Tuple[float, float, int]]:
    n = len(arr)
    if n == 1:
        return [arr[0]]
    c = mergeSort(arr[: n // 2])
    d = mergeSort(arr[n // 2 :])

    mergedArr: List[Tuple[float, float, int]] = merge(c, d)
    return mergedArr


if __name__ == "__main__":
    # fname = "input_random_13_80.txt"
    testDir = "test_cases/prob1"
    fname = f"{testDir}/scheduling.txt"
    # fname = f"{testDir}/input_random_13_80.txt"
    d: Dict[int, List[int]] = defaultdict(list)
    schedules: List[Tuple[float, float, int]] = []
    with open(fname, "r") as f:
        for line in f:
            if len(line.split()) == 1:
                continue
            weight, length = line.split()
            weight, length = int(weight), int(length)
            div = weight / length
            schedules.append((div, weight, length))
    # sort in the decreasing order of diff
    sortedSchedules = mergeSort(schedules)
    # print(*sortedSchedules, sep="\n")
    print("---------------------------------")

    weightedTimes: List[Tuple[float, float]] = []
    wlsum = 0
    lengthSum = 0
    for schedule in sortedSchedules:
        lengthSum += schedule[2]
        wl = schedule[1] * lengthSum
        wlsum += wl
        weightedTimes.append((wl, lengthSum))
    print("---------------------------------")

    # print(*weightedTimes, sep="\n")
    print(f"wl sum {wlsum}")

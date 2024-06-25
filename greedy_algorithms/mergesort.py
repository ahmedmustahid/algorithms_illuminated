from typing import List
import random


def merge(c: List[int], d: List[int]) -> List[int]:
    b: List[int] = []
    m = len(c) + len(d)
    i, j = 0, 0

    for _ in range(m):
        if c[i] < d[j]:
            b.append(c[i])
            i += 1
        elif c[i] == d[j]:
            b.append(c[i])
            i += 1
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


def mergeSort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n == 1:
        return [arr[0]]
    c = mergeSort(arr[: n // 2])
    d = mergeSort(arr[n // 2 :])

    mergedArr: List[int] = merge(c, d)
    return mergedArr


if __name__ == "__main__":
    a = list(range(11111))
    random.shuffle(a)
    # a.reverse()
    sortedArr = mergeSort(a)
    a.sort()
    print(sortedArr == a)

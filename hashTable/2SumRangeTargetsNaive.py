from typing import Set
import sys

ySet: Set[int] = set()
ySet2: Set[int] = set()
fname = "2SumChallengeCase.txt"
fname = "2SumCase_target3-10.txt"
with open(fname, "r") as f:
    for line in f:
        elem = int(line)
        if elem not in ySet:
            ySet.add(elem)


count = 0


def countTargetMatch(count: int, t: int) -> int:
    for x in ySet:
        y = t - x
        if y in ySet:
            print(f"x:{x} y:{y} count: {count}")
            count = count + 1
            ySet2.add(y)
    return count


print(sys.getsizeof(ySet))

start, stop = -(10**4), 10**4
start, stop = 3, 10
for i in range(start, stop + 1):
    print("-------------")
    print(f"target {i}")
    count = countTargetMatch(count, i)
    print("-------------")
print(f"total counts {count}")

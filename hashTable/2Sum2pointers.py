from typing import Set, List

ys: List[int] = list()
fname = "2SumCase_target3-10.txt"
fname = "2SumChallengeCase.txt"
with open(fname, "r") as f:
    for line in f:
        elem = int(line)
        ys.append(elem)
        # if elem not in ys:
        #     ys.append(elem)

ys = sorted(ys)
print(f"ys length {len(ys)}")
sums: Set[int] = set()
left, right = 0, len(ys) - 1
low, high = 3, 10
low, high = -(10**4), 10**4
while left < right:
    if (ys[left] + ys[right]) < low:
        left = left + 1
    if (ys[left] + ys[right]) > high:
        right = right - 1
    else:
        for i in range(right, left, -1):
            sum = ys[left] + ys[i]
            if sum < low:
                break
            sums.add(sum)
            # print(f"ys[left]:{ys[left]} ys[i]:{ys[i]} sum:{sum} ")
        left += 1
print(f"num of target values {len(sums)}")

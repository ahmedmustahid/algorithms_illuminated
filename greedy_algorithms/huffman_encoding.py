from typing import List, Dict, Tuple, Self
from collections import deque


class Tree:
    def __init__(self, idx: int) -> None:
        self.idx = idx
        self.left: Self | None = None
        self.right: Self | None = None
        self.rank = 0
        self.min_rank = 0

    def __repr__(self) -> str:
        return f"|{str(self.left)}" + str(self.idx) + f"{str(self.right)}|"


def initialize_trees(
    weights: List[int],
) -> Tuple[Dict[int, Tree], List[Tuple[int, int]]]:
    d: Dict[int, Tree] = {}
    trees: List[Tuple[int, int]] = []
    for i, weight in enumerate(weights):
        d[i] = Tree(i)
        trees.append((i, weight))
    return d, trees


def getWeights(fname: str) -> List[int]:
    weights = []

    with open(fname, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            weights.append(int(line))
    return weights


def merge(t1: Tree, t2: Tree, idx: int) -> Tree:
    t3 = Tree(idx)
    t3.left = t1
    t3.right = t2
    t3.rank = max(t1.rank, t2.rank) + 1
    t3.min_rank = min(t1.min_rank, t2.min_rank) + 1
    return t3


def huffman_encoding(fname: str):
    weights = getWeights(fname)
    d, trees = initialize_trees(weights)

    trees = sorted(trees, key=lambda x: x[1])
    q1, q2 = deque(trees), deque()

    merge_idx = len(d)
    while len(d) >= 2:
        if not q1 and q2:
            q1 = q2
            q2 = deque()
        if q1:
            t1 = q1.popleft()
            if q2:
                if not q1:
                    t2 = q2.popleft()
                elif q1[0][1] >= q2[0][1]:
                    t2 = q2.popleft()
                else:
                    t2 = q1.popleft()
            else:
                t2 = q1.popleft()

            t3_weight = t1[1] + t2[1]
            merge_idx += 1
            t1Idx, t2Idx = t1[0], t2[0]
            t1, t2 = d[t1Idx], d[t2Idx]
            d.pop(t1Idx)
            d.pop(t2Idx)
            t3 = merge(t1, t2, idx=merge_idx)
            q2.append((merge_idx, t3_weight))
            d[merge_idx] = t3
    return d


def maxTreeLen(tree: Tree):
    return tree.rank


def minTreeLen(tree: Tree):
    # length = 0
    # while tree is not None:
    #     if tree.left.rank <= tree.right.rank:
    #         tree = tree.left
    #         length += 1
    #     else:
    #         tree = tree.right
    #         length += 1
    # return length - 1
    return tree.min_rank


if __name__ == "__main__":
    root = "test_cases/huffman"
    # fname = "input_random_1_10.txt"
    fname = "input_random_21_320.txt"
    fname = "input_random_29_1000.txt"
    fname = "huffman_weights.txt"
    fname = f"{root}/{fname}"

    d = huffman_encoding(fname)
    tree = list(d.values())[0]
    print(f"max tree length: {maxTreeLen(tree)}")
    print(f"minimum tree length: {minTreeLen(tree)}")

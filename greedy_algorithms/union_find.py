class UnionFind:
    def __init__(self, node: str) -> None:
        self.value = node
        self.parent = self
        self.rank = 0

    def __eq__(self, other) -> bool:
        return self.value == other.value

    @staticmethod
    def count(U):
        parents = []
        for k, v in U.items():
            parent = UnionFind.find(v)
            parents.append(parent.value)
        return len(set(parents))

    @staticmethod
    def find(node):
        temp = node
        while temp.parent != temp:
            temp = temp.parent
        node.parent = temp
        return node.parent

    @staticmethod
    def union(U, x, y):
        r = UnionFind.find(x)
        s = UnionFind.find(y)

        if r.value == s.value:
            return
        if r.rank > s.rank:
            s.parent = r
        elif r.rank < s.rank:
            r.parent = s
        else:
            r.parent = s
            s.rank += 1

        U[s.value] = s
        U[r.value] = r

    def __repr__(self) -> str:
        temp = f"{self.value}->"
        node = self
        while node.parent != node:
            node = node.parent
            temp += node.value + "->"
        return temp

    @staticmethod
    def initialize(vertices):
        ufDict = {}
        for vertex in vertices:
            ufDict[vertex] = UnionFind(vertex)

        return ufDict


if __name__ == "__main__":
    uf1 = UnionFind("1")
    uf2 = UnionFind("2")
    uf3 = UnionFind("3")
    uf3.rank = 1

    U = {"1": uf1, "2": uf2, "3": uf3}
    UnionFind.union(U, uf1, uf2)
    print(f"uf2 rank {uf2.rank}")

    UnionFind.union(U, uf2, uf3)
    print(f"uf3 rank {uf3.rank}")
    print(f"uf1 rank {uf1.rank}")

    UnionFind.find(uf1)
    print(f"uf1 parent {uf1.parent}")
    print(f"uf1 parent rank {uf1.parent.rank}")

    print(f"count {UnionFind.count(U)}")

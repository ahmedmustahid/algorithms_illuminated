class UnionFind:
    def __init__(self, node: str) -> None:
        self.value = node
        self.parent = self
        self.rank = 0

    def __eq__(self, other) -> bool:
        return self.value == other.value

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
    totalNum = 10
    U = {str(i): UnionFind(str(i)) for i in range(totalNum)}
    lst = list(range(totalNum))

    for i, ls in enumerate(lst):
        if i < len(lst) - 2:
            ls = str(ls)
            UnionFind.union(U, U[ls], U[str(lst[i + 1])])
            print(f"find: {ls}, {str(lst[i + 1])}", UnionFind.find(U[ls]))
            print(U[ls])
            print("-----------")

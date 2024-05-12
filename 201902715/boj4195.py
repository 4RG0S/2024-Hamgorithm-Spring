import sys


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.count = [1 for _ in range(n)]
        self.name_to_index = {}

    def add_name_and_get_index(self, name: str) -> int:
        if name in self.name_to_index:
            return self.name_to_index[name]
        index = len(self.name_to_index)
        self.name_to_index[name] = index
        return index

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        grand_parent = self.find(self.parent[i])
        self.parent[i] = grand_parent
        return grand_parent

    def union(self, i: int, j: int) -> int:
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return self.count[parent_i]

        if self.count[parent_i] > self.count[parent_j]:
            self.parent[parent_j] = parent_i
            self.count[parent_i] += self.count[parent_j]
            return self.count[parent_i]
        else:
            self.parent[parent_i] = parent_j
            self.count[parent_j] += self.count[parent_i]
            return self.count[parent_j]


def main():
    n_test_case = int(sys.stdin.readline())
    for _ in range(n_test_case):
        n_relation = int(sys.stdin.readline())
        union_find = UnionFind(2 * n_relation)
        for _ in range(n_relation):
            i_name, j_name = sys.stdin.readline().split()
            i, j = union_find.add_name_and_get_index(i_name), union_find.add_name_and_get_index(j_name)
            print(union_find.union(i, j))


if __name__ == "__main__":
    main()

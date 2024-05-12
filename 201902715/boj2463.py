import sys


class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.count = [1 for _ in range(n)]

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        grand_parent = self.find(self.parent[i])
        self.parent[i] = grand_parent
        return grand_parent

    def union(self, i: int, j: int) -> int:
        """
        새로 발견된 u < j 의 개수를 반환한다.
        """
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return 0

        count_i = self.count[parent_i]
        count_j = self.count[parent_j]

        if self.count[parent_i] > self.count[parent_j]:
            self.parent[parent_j] = parent_i
            self.count[parent_i] += self.count[parent_j]
        else:
            self.parent[parent_i] = parent_j
            self.count[parent_j] += self.count[parent_i]

        return count_i * count_j


def main():
    N, M = map(int, sys.stdin.readline().split())
    union_find = UnionFind(N)
    inputs = []
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        inputs.append((w, u, v))
    inputs.sort(key=lambda x: -x[0])

    # [5, 4, 3, 2, 1]
    # 4인 가중치에서 경로가 추가되었다면
    # 4 + 3 + 2 + 1
    # 3인 가중치에서 경로가 추가되었다면
    # 3 + 2 + 1

    # summation_array = [15, 10, 6, 3, 1]

    summation_array = [0] * M
    for i in range(M):
        reversed_i = M - i - 1
        weight = inputs[reversed_i][0]
        if i == 0:
            summation_array[reversed_i] = weight
        else:
            summation_array[reversed_i] = summation_array[reversed_i + 1] + weight

    total_weight = 0
    for i, (w, u, v) in enumerate(inputs):
        num_of_new_connected = union_find.union(u, v)
        total_weight += num_of_new_connected * summation_array[i]
        total_weight %= 10**9

    print(total_weight)


if __name__ == "__main__":
    main()

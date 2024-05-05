def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_intersect(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.sizes = [1] * n

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.parent[a] = b
            self.sizes[b] += self.sizes[a]

    def find(self, a: int) -> int:
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def is_same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


if __name__ == "__main__":
    N = int(input())
    lines = []
    for _ in range(N):
        a1, b1, a2, b2 = map(int, input().split())
        a, b = (a1, b1), (a2, b2)
        lines.append((a, b))
    uf = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if is_intersect(*lines[i], *lines[j]):
                uf.union(i, j)

    group = {}
    max_size = 0
    for i in range(N):
        parent = uf.find(i)
        if parent not in group:
            group[parent] = []
            max_size = max(max_size, uf.sizes[parent])
    
    print(len(group))
    print(max_size)

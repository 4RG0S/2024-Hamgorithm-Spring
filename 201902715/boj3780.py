import sys
input = sys.stdin.readline
print = sys.stdout.write

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.distance_to_parent = [0] * n
    
    def find(self, x: int):
        if self.parent[x] == x:
            return x, 0
        grandparent, distance_to_grandparent = self.find(self.parent[x])
        self.parent[x] = grandparent
        self.distance_to_parent[x] += distance_to_grandparent
        return grandparent, self.distance_to_parent[x]
    
    def union(self, x: int, y: int):
        parent_x, distance_to_parent_x = self.find(x)
        parent_y, distance_to_parent_y = self.find(y)
        if parent_x == parent_y:
            return
        self.parent[parent_x] = parent_y
        self.distance_to_parent[parent_x] = distance_to_parent_y + abs(x - y) % 1000


if __name__ == "__main__":
    T = int(input().rstrip())
    for _ in range(T):
        result = ""
        N = int(input())
        union_find = UnionFind(N)
        while True:
            command = input().rstrip().split()
            if command[0] == "O":
                break
            if command[0] == "E":
                I = int(command[1])
                parent, distance = union_find.find(I - 1)
                result += "{}\n".format(distance)
            if command[0] == "I":
                I, J = map(int, command[1:])
                union_find.union(I - 1, J - 1)

        print(result)

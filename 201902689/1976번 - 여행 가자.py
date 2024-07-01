import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
m = int(input())

parent = [x for x in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if parent[a] < parent[b]:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(n):
        if tmp[j]:
            union(i + 1, j + 1)

path = list(map(int, input().split()))
prev = path[0]

for i in range(1, m):
    if find(prev) != find(path[i]):
        print("NO")
        exit(0)
    prev = path[i]
print("YES")

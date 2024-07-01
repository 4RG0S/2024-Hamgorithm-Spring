import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

parent = [x for x in range(n + 1)]

def chech_union_set(a, b):
    a = find(a)
    b = find(b)
    print("yes") if a == b else print("no")

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    op, a, b = map(int, input().split())
    if op: # find
        chech_union_set(a, b)
    else: # union
        union(a, b)

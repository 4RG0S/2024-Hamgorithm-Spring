import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if parent[a] < b:
            parent[b] = a
            size[a] += size[b]
        else:
            parent[a] = b
            size[b] += size[a]
        print(size[parent[a]])
    else:
        print(size[parent[a]])

for _ in range(t):
    f = int(input())
    f_set = set()
    parent = [x for x in range(f * 2)]
    size = [1 for _ in range(f * 2)]
    dictionary = dict()
    for _ in range(f):
        a, b = map(str, input().split())
        if a not in f_set:
            dictionary[a] = len(f_set)
            f_set.add(a)
        if b not in f_set:
            dictionary[b] = len(f_set)
            f_set.add(b)
        union(dictionary[a], dictionary[b])

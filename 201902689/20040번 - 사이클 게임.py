import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [x for x in range(n)]
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if parent[a] > b:
            parent[a] = b
            size[b] = size[parent[a]]
        else:
            parent[b] = a
            size[a] = size[parent[b]]
    else: # 최상위 노드가 같아서 사이클 발생함
        return True
    return False


for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        print(i + 1)
        exit(0)
print(0)

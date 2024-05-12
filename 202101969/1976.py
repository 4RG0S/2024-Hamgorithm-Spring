import sys

def union(x, y, parents):
    x_root = find(x, parents)
    y_root = find(y, parents)

    if x_root < y_root:
        parents[y_root] = x_root
    else:
        parents[x_root] = y_root

def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parents = [i for i in range(n)]
for i in range(n):
    link = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if link[j] == 1:
            union(i, j, parents)

parents = [-1] + parents
path = list(map(int, sys.stdin.readline().split()))
start = parents[path[0]]
for i in range(1, m):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
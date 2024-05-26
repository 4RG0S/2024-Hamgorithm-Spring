import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    node = list(map(int, input().split()))[:-1]
    for i in range(1, len(node)//2 + 1):
        graph[node[0]].append([node[i*2 - 1], node[i*2]])

def dfs(x, dist):
    for i in graph[x]:
        node, wei = i
        if distance[node] == -1:
            distance[node] = dist + wei
            dfs(node, dist + wei)

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

res = distance.index(max(distance))
distance = [-1] * (n+1)
distance[res] = 0
dfs(res, 0)

print(max(distance))
import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(s):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    queue = deque()
    queue.append((s, 0))
    visited[s] = True
    while queue:
        current, acc = queue.popleft()
        for (node, cost) in graph[current]:
            if not visited[node]:
                distance[node] = cost + acc
                queue.append((node, distance[node]))
                visited[node] = True
    return distance.index(max(distance)), max(distance)

node, cost = bfs(1)
_, result = bfs(node)
print(result)

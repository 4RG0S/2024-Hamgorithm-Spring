import sys
from collections import deque

def dfs(V):
    visited_1[V] = 1
    print(V, end=" ")

    for node in graph[V]:
        if not visited_1[node]:
            dfs(node)
def bfs(V):
    q = deque()
    q.append(V)
    visited_2[V] = 1
    while q:
        x = q.popleft()
        print(x, end=" ")
        for node in graph[x]:
            if not visited_2[node]:
                q.append(node)
                visited_2[node] = 1
N,M,start = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited_1 = [0] *(N+1)
visited_2 = visited_1.copy()

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(start)
print()
bfs(start)
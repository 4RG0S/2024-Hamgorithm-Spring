import sys
sys.setrecursionlimit(10 ** 5)


def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)

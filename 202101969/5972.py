import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
inf = 1e8

graph = [[] for _ in range(n+1)]

distance = [inf] * (n+1)

for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(1)
print(distance[n])
from collections import deque
import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))


def dijkstra(s, e):
    dist = [INF] * (n + 1)
    dist[s] = 0
    queue = []
    heapq.heappush(queue, (dist[s], s))
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if dist[current_node] < current_dist:
            continue

        for (next_node, cost) in graph[current_node]:
            distance = cost + dist[current_node]
            if dist[next_node] > distance:
                dist[next_node] = distance
                heapq.heappush(queue, (distance, next_node))
    return dist[e]

result = 0
for i in range(1, n +1):
    result = max(result, (dijkstra(i, x) + dijkstra(x, i)))

print(result)

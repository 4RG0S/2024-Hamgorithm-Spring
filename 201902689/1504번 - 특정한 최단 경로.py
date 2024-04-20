import heapq
import sys
import copy
input = sys.stdin.readline
INF = float("inf")
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
 
v1, v2 = map(int, input().split())
 
def dijkstra(s, e):
    copiedDistance = copy.deepcopy(distance)
    queue = []
    heapq.heappush(queue, (0, s))
    copiedDistance[s] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        for (node, weight) in graph[now]:
            tmp = weight + cost
            if copiedDistance[node] > tmp:
                copiedDistance[node] = tmp
                if node == e:
                    continue
                heapq.heappush(queue, (tmp, node))
    return copiedDistance[e] 

result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
result2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
result = min(result1, result2)
if result == INF:
    print(-1)
else: print(result)
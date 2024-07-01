import heapq

def dijikstra(graph, N, s, e):
    dist = [int(1e9)] * (N+1)
    dist[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:
            continue

        for nxt, n_cost in graph[node]:
            c = cost + n_cost
            if c < dist[nxt]:
                dist[nxt] = c
                heapq.heappush(pq, (c, nxt))

    print(dist[e])

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append([y, cost])
start, end = map(int, input().split())

dijikstra(graph, N, start, end)
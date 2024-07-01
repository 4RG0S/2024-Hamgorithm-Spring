import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())

graph = []
distance = [[INF for _ in range(m)] for _ in range(n)]
distance[0][0] = 0

def check(y, x):
    return 0 <= y < n and 0 <= x < m

for _ in range(n):
    line = input()
    graph.append(line)

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        current_dist, (y, x) = heapq.heappop(queue)
        if distance[y][x] < current_dist:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if check(ny, nx):
                spot = graph[ny][nx]
                if spot == '0':
                    if current_dist < distance[ny][nx]:
                        heapq.heappush(queue, (current_dist, (ny, nx)))
                        distance[ny][nx] = current_dist
                else:
                    if current_dist + 1 < distance[ny][nx]:
                        heapq.heappush(queue, (current_dist+1, (ny, nx)))
                        distance[ny][nx] = current_dist+1
    return distance[n-1][m-1]

result = dijkstra()

print(result)
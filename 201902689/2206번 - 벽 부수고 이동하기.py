import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
distance = [[[0] * 2 for _ in range(m)] for _ in range(n)]
distance[0][0][0] = 1
for _ in range(n):
    graph.append(input().strip())
def check(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(y, x):
    queue = deque()
    queue.append((y, x, 0))

    while queue:
        y, x, drill = queue.popleft()
        if y == n-1 and x == m-1:
            return distance[y][x][drill]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if check(ny, nx):
                if graph[ny][nx] == '1' and drill == 0: # 다음 위치가 벽이고, 아직 벽 파괴를 한 적이 없음
                    distance[ny][nx][1] = distance[y][x][0] + 1
                    queue.append((ny, nx, 1))
                elif graph[ny][nx] == '0' and distance[ny][nx][drill] == 0:
                    distance[ny][nx][drill] = distance[y][x][drill] + 1
                    queue.append((ny, nx, drill))
    return -1

result = bfs(0, 0)
print(result)
"""
반례

6 5
00000
11110
00000
01111
01111
00010

output: 18
"""
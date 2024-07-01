import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:   # 아직 방문 안 했으면
                if arr[nx][ny] == 0:    # 막혀 있는 땅
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:  # 갈 수 있는 땅
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))  # 큐에 넣어줌으로써 다음 경로 탐색

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:   # 시작지점 발견
            bfs(i, j)   # 탐색 시작

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
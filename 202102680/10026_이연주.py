import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

array = [list(input().rstrip()) for _ in range(n)]   # 그림 입력 받기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs_first(a,b, color):
    dq = deque()
    dq.append([a,b])
    visited[a][b] = True    # 방문한 곳 체크

    while dq:
        i,j = dq.pop()

        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                continue

            if color == array[x][y]:
                visited[x][y] = True
                dq.append([x,y])
    return

def bfs_second(a,b,color):
    dq = deque()
    dq.append([a,b])

    visited[a][b] = True
    while dq:
        i,j = dq.pop()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                continue

            if color != 'B' and array[x][y] != 'B':
                visited[x][y] = True
                dq.append([x, y])
            elif color == 'B' and array[x][y] == 'B':
                visited[x][y] = True
                dq.append([x, y])
    return


visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_first(i,j,array[i][j])
            count += 1

print(count, end=' ')
visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_second(i,j,array[i][j])
            count += 1

print(count)
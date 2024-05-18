from collections import deque

h, w = map(int, input().split())
matrix = [input() for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    visit = [[0 for _ in range(w)] for _ in range(h)]
    visit[i][j] = 1

    cnt = 0
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and \
                matrix[nx][ny] == 'L' and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y]+1
                cnt = max(cnt, visit[nx][ny])
                que.append((nx, ny))
    return cnt-1

ans=0
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 'W':
            continue
        ans = max(ans, bfs(i, j))
print(ans)
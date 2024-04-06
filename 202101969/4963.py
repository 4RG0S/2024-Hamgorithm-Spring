import sys
from collections import deque

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1,-1, 0, 0, 1, 1, 1]
def bfs(new_y, new_x):
    queue = deque()
    queue.append((new_y, new_x))
    # 방문지 작성 추가
    visited[new_y][new_x] = True

    while queue:
        y,x = queue.popleft()
        m_ap[y][x] = 0
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < h) and (0 <= nx < w) and m_ap[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

while True:
    c = 0
    w,h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    m_ap = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if m_ap[y][x] == 1:
                bfs(y,x)
                c +=1
    print(c)
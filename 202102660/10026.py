import sys
from collections import deque

sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
grid = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited_2 = [[0]*N for _ in range(N)]

queue = deque()
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

def is_in_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def is_same_for_wrong(nx, ny, x, y):
    if ((grid[nx][ny] == "G" or grid[nx][ny] == "R") and (grid[x][y] == "G" or grid[x][y] == "R")):
        return True
    elif grid[nx][ny] == grid[x][y]:
        return True
    else: return False

def BFS(wrong):
    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if wrong:
                if is_in_range(nx, ny) and not visited_2[nx][ny]:
                    if is_same_for_wrong(nx, ny, x, y):
                        queue.append((nx, ny))
                        visited_2[nx][ny] = 1
            else:
                if is_in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

def DFS(wrong):
    if queue:
        (x, y) = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if wrong:
                if is_in_range(nx, ny) and not visited_2[nx][ny]:
                    if is_same_for_wrong(nx, ny, x, y):
                        queue.append((nx, ny))
                        visited_2[nx][ny] = 1
                        DFS(wrong)
            else:
                if is_in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    DFS(wrong)
    else: return

count = 0
count_2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            queue.append((i, j))
            # BFS(False)
            DFS(False)
            count += 1

for i in range(N):
    for j in range(N):
        if not visited_2[i][j]:
            queue.append((i, j))
            # BFS(True)
            DFS(True)
            count_2 += 1

print(count, count_2)
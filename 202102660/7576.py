import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]
# visited = [[0]*M for _ in range(N)]
que = deque()

def is_in_range(x, y):
    # 좌표가 범위를 넘어갔는지 확인
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def BFS():
    while que:
        (x, y) = que.popleft()
        # visited[x][y] = 1 # 방문 처리
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동, 남, 서, 북 # x가 세로
        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            if is_in_range(nx, ny) and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                que.append((nx, ny))



for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            que.append((i, j))

BFS()
flag_0, flag_1 = False, False
# print(box)
for b in box:
    if 0 in b:
        # 0 이 존재 -> 모든 토마토가 익지 않음
        flag_0 = True

    if 1 in b:
        # 1이 존재 -> 토마토 익힐 수 있다.
        flag_1 = True

# print(flag_0, flag_1)
if flag_1 and not flag_0: print(max(map(max, box))-1)
elif not flag_1 or flag_0: print("-1")

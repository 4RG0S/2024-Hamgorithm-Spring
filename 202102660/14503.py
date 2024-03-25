'''
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    - 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    - 반시계 방향으로 90도회전한다.
    - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    - 1번으로 돌아간다.
'''

## 3번에서 1번으로 돌아갈때, 앞으로 이동하지 않은 경우에 대해서도 stack에 추가해야함!!
import sys
from collections import deque

(n, m) = map(int, sys.stdin.readline().split())
(r, c, d) = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북, 동, 남, 서
count = 0
stack = deque()

def is_any_uncleaned(x, y):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if  0< nx < n-1 and 0< ny < m-1 and room[nx][ny] == 0:
            return True
    return False

def move_ahead(x, y, d):
    nx, ny = x + dx[d], y + dy[d]
    if 0< nx < n-1 and 0< ny < m-1 and room[nx][ny] == 0:
        return (True, nx, ny, d)
    return (False, x, y, d)

def move_back(x, y, d):
    nx, ny = x - dx[d], y - dy[d]
    if 0< nx < n-1 and 0< ny < m-1 and room[nx][ny] != 1:
        return (True, nx, ny, d)
    return (False, x, y, d)

def dfs():
    global count
    while stack:
        (x, y, d) = stack.pop()
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if room[x][y] == 0:
            room[x][y] = 2
            count += 1
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if not is_any_uncleaned(x, y):
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            (can_go, nx, ny, d) = move_back(x, y, d)
            if can_go:
                stack.append((nx, ny, d))
                continue
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            # 반시계 방향으로 90도회전한다.
            nd = (d-1)%4
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            (can_go, nx, ny, nd) = move_ahead(x, y, nd)
            if can_go:
                stack.append((nx, ny, nd))
            # 1번으로 돌아간다.
            else: stack.append((x, y, nd))
            continue
            
stack.append((r, c, d))   
dfs()
print(count)


        
        


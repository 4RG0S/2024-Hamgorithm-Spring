
# 1. 초기 R, B 위치 저장
# 2. 그 위치 큐에 넣기, 방문처리, BFS호출
# BFS
# 1. 큐에 있는거 뺌.
# 2. 뺀 위치 움직이기 (# 만나거나 o 만날때까지)
    # 1. 4가지 방향에 대해 (이때 왔던 방향으로 돌아가는 방향 제외안해도 됨. 방문 여부에서 걸러짐)
    # 2. #이나 o 만나면 (#일 경우-d[d]한) 위치가 방문한 곳이 아니라면 큐에 추가
    # 3. b가 o 들어갔으면 continue
    # 4. r만 o 들어갔으면 프린트(count), exit(0)
    # 5. 둘 다 안들어갔고, 만약 r, b위치가 같다면 더 많이 움직인 애를 -dx[d], -dy[d]함
    # 6. 방문 하지 않은 위치 조합이면 방문처리 후 큐에 넣기
# print(-1)

## 방문 처리 까먹음
## [rx, ry, bx, by] 조합으로 접근했는지 안했는지 확인해야함!!
## R이 안움직였어도, B는 움직여서 R이 o에 빠지도록 기여했을 수 있음

import sys
from collections import deque

(n, m )= tuple(map(int, sys.stdin.readline().split()))
board = [list(sys.stdin.readline()) for _ in range(n)]
visited = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
que = deque()
count = 0

def in_hole(x, y):
    if board[x][y] == 'O': return True
    return False

def how_far(x, y, d):
    for h in range(1, max(n, m)-1):
        nx, ny = x + h*dx[d], y + h*dy[d]
        if not (0 <= nx < n and 0 <= ny < m): return h-1
        if board[nx][ny] == '#':
            return h-1
        if board[nx][ny] == 'O':
            return h
    return 0

def BFS():
    min_count = sys.maxsize
    while que:
        (rx, ry, bx, by, count) = que.popleft()
        # print(f'pop: {rx}, {ry}, count: {count}')
        # if count >= 10: continue
        # if d != -1: # -1인 경우는 초기 위치
        #     if in_hole(bx, by): continue
        #     elif in_hole(rx, ry):
        #         print(count)
        #     # 둘 다 안들어 간 경우
        #     if (rx == bx) and (ry == by):
        #         if rh > bh:
        #             rx -= dx[d]
        #             ry -= dy[d]
        #         else:
        #             bx -= dx[d]
        #             by -= dy[d]
        # 기울기기 시작
        for nd in range(4):
            nrh = how_far(rx, ry, nd)
            nbh = how_far(bx, by, nd)
            nrx, nry = rx + nrh*dx[nd], ry + nrh*dy[nd]
            nbx, nby = bx + nbh*dx[nd], by + nbh*dy[nd]
            if in_hole(nbx, nby): continue
            elif in_hole(nrx, nry):
                print(count+1)
                exit(0)
            # 둘 다 안들어 간 경우
            if (nrx == nbx) and (nry == nby):
                if nrh > nbh:
                    nrx -= dx[nd]
                    nry -= dy[nd]
                else:
                    nbx -= dx[nd]
                    nby -= dy[nd]
                # if rx == 4 and ry == 8: print(f'visited[{nrx}][{nry}]: {visited[nrx][nry]}')
            if [nrx, nry, nbx, nby] not in visited:
                visited.append([nrx, nry, nbx, nby])
                # print(f'append: {nrx} {nry}')
                que.append((nrx, nry, nbx, nby, count+1))
    print(-1)


# 초기 R, B 위치 구하기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

que.append((rx, ry, bx, by, count))

visited.append([rx, ry, bx, by])

BFS()
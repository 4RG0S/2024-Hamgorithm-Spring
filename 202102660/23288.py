## 맨 처음 큐에 넣는 원소 방문처리, 점수 추가 까먹음!!!
from collections import deque
# 주사위 굴리기
def roll(x, y, d):
    # 북, 남은 그냥 한줄만 로테이션
    new_dice = [d[:] for d in dice]
    if d == 1:
        # 남쪽인경우
        for i in range(4):
            if i == 0:
                dice[1][1] = new_dice[i][0]
            elif i == 1:
                dice[2][0] = new_dice[i][1]
            else:
                dice[(i+1)%4][0] = new_dice[i][0]
    elif d == 3:
        # 북
        for i in range(4):
            if i == 1:
                dice[0][0] = new_dice[1][1]
            elif i == 2:
                dice[1][1] = new_dice[2][0]
            else:
                dice[(i-1)%4][0] = new_dice[i][0]
    elif d == 0:
        # 동쪽인 경우
        for j in range(3):
            if j == 2:
                dice[3][0] = new_dice[1][2]
                dice[1][0] = new_dice[3][0]
            else: dice[1][j+1] = new_dice[1][j]
    elif d == 2:
        # 서
        for j in range(3):
            if j == 0:
                dice[3][0] = new_dice[1][j]
                dice[1][2] = new_dice[3][0]
            else: dice[1][j-1] = new_dice[1][j]
    return x+dx[d], y+dy[d]


# 칸 스코어 계산
def get_score(x, y):
    global N, M
    num = board[x][y]
    visited = [[0]*M for _ in range(N)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    count = 1
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == num:
                visited[nx][ny] = 1
                que.append((nx, ny))
                count += 1
    return count*num

def get_dir(x, y, d):
    global N, M
    '''
    주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    A = B인 경우 이동 방향에 변화는 없다.
    '''
    A = dice[3][0]
    B = board[x][y]
    if A > B: d = (d+1)%4
    elif A < B: d = (d-1)%4

    # 바꾼 방향으로 가려고 할때 그 방향이 범위를 벗어나는 방향이면 반대로 바꿈
    nx, ny = x + dx[d], y + dy[d]
    if not(0<=nx<N and 0<=ny<M): d = (d+2)%4

    return d


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북
dice = [    [2],
         [4, 1, 3],
            [5],
            [6]
        ]
d = 0
x, y = 0, 0
score = 0
for _ in range(K):
    x, y = roll(x, y, d)
    score += get_score(x, y)
    d = get_dir(x, y, d)

print(score)


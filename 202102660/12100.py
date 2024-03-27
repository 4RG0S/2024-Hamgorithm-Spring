## 같은 board에 대해 4방향으로 움직일때, board의 상태는 변하면 안되므로 -> deepcopy 이용!!

# (최대 5번)
# 상, 하, 좌, 우 움직이기
# 움직일때
    # 가고자 하는 방향의 제일 선두부터. (위로 가면 0번째 행, 왼쪽으로 가면 0번째 열, ...)
    # 같은 라인에 제일 가까운(가고자 하는 방향의 반대방향으로 찾았을때) 블럭과 합치기. (합친 원래 블럭들의 위치는 0으로 바뀜)
    # 합친건 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
    # 이 과정을 모든 라인에 대해 반복
# 다 움직였으면 count +1
# 5가 되면 제일 큰 원소 찾아서 list에 추가

# 마지막엔 list에서 제일 큰 원소 프린트
import sys
from collections import deque
from copy import deepcopy

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오른쪽, 아래, 왼쪽
result = [] # 최대값 저장
stack = deque()
visited = []

# 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
def can_go(d, i, j, board):
    ii, jj = i, j
    new_i, new_j = i, j
    while True:
        new_i, new_j = new_i + dx[d], new_j + dy[d]
        if not (0<=new_i<N and 0<=new_j<N): break
        if board[new_i][new_j] == 0:
            ii, jj = new_i, new_j
        else: break
    num = board[i][j]
    board[i][j] = 0
    board[ii][jj] = num
    # print(i, j, ii, jj)
    return board

def concat(i, j, d, board):
    # (i, j)와 합칠 수 있는 블럭 찾기
    new_i, new_j = i, j
    dd = (d+2)%4 # 반대 방향
    while True:
        new_i, new_j = new_i + dx[dd], new_j + dy[dd]
        if not (0<=new_i<N and 0<=new_j<N): return board # 범위 벗어남
        if board[i][j] == board[new_i][new_j]:
            board[i][j] *= 2
            board[new_i][new_j] = 0
            return board
        else:
            if board[new_i][new_j] != 0: return board
    
def move(d, board):
    # 가고자 하는 방향의 제일 선두부터. (위로 가면 0번째 행, 왼쪽으로 가면 0번째 열, ...)
    # 같은 라인에 제일 가까운(가고자 하는 방향의 반대방향으로 찾았을때) 블럭과 합치기. (합친 원래 블럭들의 위치는 0으로 바뀜)
    # 합친건 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
    # 이 과정을 모든 라인에 대해 반복
    if d == 0: # 위
        # 모든 열에 대해서
        for j in range(N):
            # 각 행
            for i in range(N):
                board = concat(i, j, d, board)
                # 합친건(합쳤든 안합쳤든) 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
                board = can_go(d, i, j, board)
    elif d == 1: # 오른쪽
        # 모든 행에 대해서
        for j in range(N):
            # 각 열
            for i in range(N-1, -1, -1):
                board = concat(j, i, d, board)
                # print(board)
                # 합친건(합쳤든 안합쳤든) 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
                board = can_go(d, j, i, board)
    
    elif d == 2: # 아래
        # 모든 열에 대해서
        for j in range(N):
            # 각 행
            for i in range(N-1, -1, -1):
                board = concat(i, j, d, board)
                # 합친건(합쳤든 안합쳤든) 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
                board = can_go(d, i, j, board)
        
    elif d == 3:
        # 모든 행에 대해서
        for j in range(N):
            # 각 열
            for i in range(N):
                board = concat(j, i, d, board)
                # 합친건(합쳤든 안합쳤든) 가고자 하는 방향으로 갈 수 있는 만큼 가서 놓기.
                board = can_go(d, j, i, board)
    return board
        
    
def game():
    while stack:
        (count, board) = stack.pop()
        # print(xboard)
        # 5가 되면 제일 큰 원소 찾아서 list에 추가
        if count == 5:
            result.append(max(map(max, board)))
            continue
  
        # 상, 하, 좌, 우 움직이기
        for d in range(4):
            # if d == 1: print(board)
            nboard = move(d, deepcopy(board))
            # 움직였으면 stack에 append
            if (count+1, nboard) not in visited:
                stack.append((count+1, nboard))
                visited.append((0, nboard))
    
    print(max(result))

stack.append((0, board))
visited.append((0, board))
game()
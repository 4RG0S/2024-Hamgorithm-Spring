from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = list(map(int, sys.stdin.readline().split()))
board = []
queue = deque() # [x, y, day]
result = 0

for row in range(N):
  lst = list(map(int, sys.stdin.readline().split()))
  for col in range(M):
    if lst[col] == 1:
      queue.append([col, row, 0])
  board.append(lst)

while len(queue) > 0:
  x, y, day = queue.popleft()
  result = day
  for i in range(4):
    next_x = x + dx[i]
    next_y = y + dy[i]
    if 0 <= next_x and next_x < M and 0 <= next_y and next_y < N and board[next_y][next_x] == 0:
      board[next_y][next_x] = 1
      queue.append([next_x, next_y, day + 1])

is_all_rotten = True

for row in range(N):
  for col in range(M):
    if board[row][col] == 0:
      is_all_rotten = False

print(-1 if is_all_rotten == False else result)

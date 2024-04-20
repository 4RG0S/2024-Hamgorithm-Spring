import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = []
visited = [[False] * c for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(r):
    tmp = input()
    board.append(tmp)


def check(y, x):
    return 0 <= y < r and 0 <= x < c and not visited[y][x]

def dfs(y, x, count):
    global max_count
    max_count = max(max_count, count)
    visited[y][x] = True
    asc = ord(board[y][x]) - 65
    alpha[asc] = True
    for i in range(4):
        ny, nx = y + dy[i],  x + dx[i]
        if check(ny, nx) and board[ny][nx]:
            asc = ord(board[ny][nx]) - 65
            if not alpha[asc]:
                dfs(ny, nx, count + 1)
                visited[ny][nx] = False
                alpha[asc] = False

max_count = 1
alpha = [False] * 26
dfs(0, 0, 1)
print(max_count)
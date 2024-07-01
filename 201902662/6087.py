from collections import deque
Inf = float('inf')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def main():
    w, h = map(int, input().split())
    board = [input() for _ in range(h)]
    
    c = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'C':
                c.append((i, j))

    que = deque()
    mirror = [[[Inf for _ in range(4)] for _ in range(w)] for _ in range(h)]
    
    x, y = c[0]
    for d in range(4):
        que.append((x, y, d))
        mirror[x][y][d] = 0
    
    while que:
        x, y, d = que.popleft()
        for i in range(3):
            nd = (d+i-1)%4
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
                cnt = mirror[x][y][d]
                
                if i != 1:
                    cnt += 1
                
                if mirror[nx][ny][nd] > cnt:
                    que.append((nx, ny, nd))
                    mirror[nx][ny][nd] = cnt

    x, y = c[1]
    print(min(mirror[x][y]))
    
if __name__ == "__main__":
    main()
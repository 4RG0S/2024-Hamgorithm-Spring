import sys

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = [(x, y)]
    land[x][y] = -1
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = -1

if __name__ == '__main__':
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().strip().split(' '))
        land = [[0] * M for _ in range(N)]
        
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().strip().split(' '))
            land[y][x] = 1

        worm = 0
        for i in range(N):
            for j in range(M):
                if land[i][j] == 1:
                    bfs(i, j)
                    worm += 1
        print(worm)
                
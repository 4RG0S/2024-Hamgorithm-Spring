dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y) :
    q = [(x, y)]
    matrix[x][y] = 0

    while q :
        x, y = q.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if matrix[nx][ny] == 1 :
                matrix[nx][ny] = 0
                q.append((nx, ny))
    return

tc = int(input())
result = []

for _ in range(tc) :
    count = 0
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k) :
        tmp_x, tmp_y = map(int, input().split())
        matrix[tmp_y][tmp_x] = 1
    for a in range(n) :
        for b in range(m) :
            if matrix[a][b] == 1 :
                BFS(a, b)
                count += 1
    result.append(count)

for i in result :
    print(i)
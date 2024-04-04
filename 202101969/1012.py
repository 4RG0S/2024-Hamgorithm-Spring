import sys
from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, 1, -1]


def bfs(y, x):
    queue = deque()
    queue.append((y,x))
    graph[y][x] = 0

    while queue:
        yy, xx = queue.popleft()
        for find1 in range(4):
            ny = yy + dy[find1]
            nx = xx + dx[find1]
            if (0 <= nx < M_) and (0 <= ny < N_l) and (graph[ny][nx] == 1):
                queue.append((ny, nx))
                graph[ny][nx] = 0

T = int(sys.stdin.readline())
for _ in range(T):
    M_, N_l, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M_ for _ in range(N_l)]
    for _ in range(K):
        # X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    count = 0
    for n_l in range(N_l):
        for m_ in range(M_):
            if graph[n_l][m_] == 1:
                bfs(n_l, m_)
                count +=1
    print(count)
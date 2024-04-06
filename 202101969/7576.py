import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        temp_y,temp_x = queue.popleft()
        for i in range(4):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if (0 <= nx < G_) and (0 <= ny < S_l) and graph[ny][nx] == 0:
                graph[ny][nx] = graph[temp_y][temp_x]+ 1
                queue.append((ny, nx))


graph = []
is_all = True # tomato가 모두 익어있다
G_, S_l = map(int, sys.stdin.readline().split())
queue = deque()
for i in range(S_l):
    a = list(map(int, sys.stdin.readline().split()))
    graph.append(a)

for it_y in range(S_l):
        for it_x in range(G_):
            if graph[it_y][it_x] == 1:
                queue.append((it_y, it_x))
            if graph[it_y][it_x] == 0:
                is_all = False # no! 안익은게 하나라도 있다
bfs()
m = 0
find_zero = False
for y in range(len(graph)):
    for x in range(len(graph[0])):
        m = max(m, graph[y][x])
        if graph[y][x] == 0:
            find_zero = True
            break

if is_all == True:
    print(0)
elif find_zero == True:
    print(-1)
else:
    #다 익는 상황
    print(m-1)

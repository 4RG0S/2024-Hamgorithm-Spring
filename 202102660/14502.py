## visited 필요없음!!
## 각 wall 조합에 대해 bfs할때 처음에 초기화했던 큐로 시작해야함!! (한번 돌고나면 없어짐)
'''
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.
'''
'''
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

'''
import sys
from itertools import combinations
from collections import deque
N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
empty = []
wall_list = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
que = []

def is_in_range(x,y):
    if 0 <= x < N and 0 <= y < M: return True
    return False

def bfs(wall_lab):
    nque = deque(que)
    while nque:
        (x, y) = nque.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if is_in_range(nx, ny) and wall_lab[nx][ny] == 0:
                wall_lab[nx][ny] = 2
                nque.append((nx, ny))
    return wall_lab

def each_case(wall):
    wall_lab = [l[:] for l in lab]
    # 벽 세우기
    for (x, y) in wall:
        wall_lab[x][y] = 1
        
    wall_lab = bfs(wall_lab)
    return wall_lab


def set_wall():
    wall_list = combinations(empty, 3)
    return wall_list

def find_empty():
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                empty.append((i, j))
                
def count_safe(wall_lab):
    cnt = 0
    for line in wall_lab:
        for l in line:
            if l == 0: cnt += 1
    return cnt

find_empty()
wall_list = set_wall()
max_cnt = -1
# 초기 바이러스 발생지 큐에 추가 및 방문처리
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            que.append((i, j))
# 가능한 모든 벽 조합에 대해 bfs 돌기
for wall in wall_list:
    wall_lab = each_case(wall)
    max_cnt = max(max_cnt, count_safe(wall_lab))

print(max_cnt)
    

        

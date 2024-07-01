## 그냥 dfs로 구현하면 편함.
## 기준 씨씨티비 이후의 씨씨티비를 검사하는 부분을 생각없이 구현해서 이상했음.

'''
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.
'''
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
office = [list( map(int, sys.stdin.readline().split())) for _ in range(N)]

# 완전탐색
# 씨씨티비를 각각 모든 방향에 대해 나올 수 있는 경우 다 구하기
# (1: 4, 2: 2, 3: 4, 4: 4, 5: 1) {1: [(0), (1), (2), (3)], 2: [(0, 1), (1, 2), (3, 4), (0, 4)], ...}
# 방향들의 모든 경우의 수에 대해 dfs 
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위 오 아 왼
stack = deque()
d_list = {1: [[0], [1], [2], [3]], 3: [[0, 1], [1, 2], [2, 3], [3, 0]],
          2: [[1, 3], [0, 2]], 4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
          5: [[0, 1, 2, 3]] 
          }
min_count = sys.maxsize
# 주어진 방향에 대해 # 처리
def sharp(d, x, y, office):
    for i in range(max(N, M)):
        nx, ny = x+dx[d]*i, y+dy[d]*i
        if 0<=nx<N and 0<=ny<M:
            # 벽 만나면 멈춤
            if office[nx][ny] == 6: break
            elif office[nx][ny] == 0: office[nx][ny] = '#'
        else: break

def count_zero(office):
    cnt = 0
    for o in office:
        for num in o:
            if num == 0: cnt += 1
    return cnt

def dfs(x, y, office):
    global min_count
    # 매개변수로 받은 좌표의 이후에 있는 씨씨티비 조사
    last_one = True
    for i in range(x, N):
        yy = y+1 if i == x else 0
        for j in range(yy, M):
            if office[i][j] != '#' and 1<=office[i][j]<=5:
                # 씨씨티비 찾음.
                last_one = False
                # 이 씨씨티비가 가질 수 있는 모든 방향에 대해 # 처리 하기.
                cctv = office[i][j]
                # print(d_list[cctv], i, j)
                for ds in d_list[cctv]:
                    d_office = [o[:] for o in office]
                    for d in ds:
                        sharp(d, i, j, d_office) 
                    # 하나의 경우의 수에 대한 샵처리 끝남
                    # dfs 호출 (office 깊은 복사해서)
                    dfs(i, j, d_office)
                return
    if last_one:
        min_count = min(min_count, count_zero(office))
        return

# 방향 리스트의 모든 조합에 대해 visited 리스트를 만들어서 그 방향이고, 방문하지 않은 좌표이며 0이 아닌 경우 셈. (벽만나면 멈추기)
# 전체 수에서 위에서 센 만큼을 빼면 사각지대 수
# 아 그냥 샵처리하고 그때그때 dfs??
dfs(0, -1, office)
print(min_count)

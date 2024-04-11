## 원래 바이러스였던 애들은 제외
## N을 M으로 오타냄!
## 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
## 비활성 바이러스만 남은 경우 굳이 시간 쓰지말고 그냥 종료해야함. 근데 이걸 일일이 확인할순 없으니까
## 그래서 비활성 바이러스에 대해서는 맵에 *로 표기, 벽인경우 -로 표기, 애초에 활성인경우도 *-> 마지막에 제일 큰 수 찾을 때 제대로 찾기 가능

'''
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 
놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 
0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
'''
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
# 초기 바이러스 위치 저장리스트
init_viruses = []
que = deque()
min_last = 100000
final = False
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
# 초기 바이러스 위치 찾으면서 전처리
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1: lab[i][j] = '-'
        if lab[i][j] == 2: 
            lab[i][j] = '*'
            init_viruses.append((i, j))
        
def spread(activated):
    # BFS
    visited = [[0]*N for _ in range(N)]
    nlab = [l[:] for l in lab]
    # last = 0
    # 일단 activated에 있는 좌표들 que에 넣음
    for xy in activated:
        que.append((xy, 0)) # ((x, y), t)
        # nlab[xy[0]][xy[1]] = '*'
        visited[xy[0]][xy[1]] = 1 # 방문처리
    
    while que:
    # que에 있는거 빼고
        ((x, y), t) = que.popleft()
    # 4방향에 대해 방문X인 위치이고, 벽, 범위 확인 후 갈 수 있으면 시간 찍을때 last변수도 업뎃! que에 넣고 방문처리
        for d in range(4):
            nx, ny = x +dx[d], y + dy[d]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and lab[nx][ny] != '-':
                if lab[nx][ny] != '*': # 비활성이 아닌 애들만 맵에 업뎃
                    nlab[nx][ny] = t+1
                que.append(((nx, ny), t+1))
                # last = t+1
                visited[nx][ny] = 1
            # if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and lab[nx][ny] == 1: nlab[nx][ny] = '-'
    # 다 확인했으면
    # 배열에 0있나 확인하면서 최대값 구하기. 없으면 True, last 리턴. 있으면 (False, last)
    max_num = 0
    flag = True
    for i in range(N):
        for j in range(N):
            if str(nlab[i][j]).isdecimal():
                if nlab[i][j] == 0:
                    flag = False
                max_num = max(max_num, nlab[i][j])
    # print(nlab)
    return flag, max_num

# 초기 바이러스들 중 활성으로 변경할 수 있는 조합 찾기
def collect(i, activated):
    global M, min_last, final
    # n의 값이 m이 되면 완성이므로 바이러스 퍼뜨리기 시뮬
    if len(activated) == M:
        # print(activated)
        completed, last = spread(activated)
        if completed: 
            min_last = min(min_last, last)
            final = True # 한번이라도 다 퍼뜨려지면 True 됨.
        return
    # 아니면
    for idx in range(i+1, len(init_viruses)):
        # 이미 넣어진 애 이후부터 탐색 (조합이니까)
        collect(idx, activated +[init_viruses[idx]])
    return 

collect(-1, [])
if final: print(min_last)
else: print(-1)
    
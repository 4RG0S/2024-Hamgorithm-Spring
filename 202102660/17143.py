## 좌표 시작점 0으로 착각
## 상어 이동 구현 방법 잘못함
## 상어 잡히거나 먹히거나 이동하거나 할때 살아있는 상어에 대해서만 하는 것 까먹음
## 상어 이동 시 s를 처음에 나머지 연산으로 줄일 수 있을만큼 줄이기
## sea 배열을 하나 만들어서 불필요한 반복문 줄이기

'''
첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)

둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.

두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
'''
import sys

R, C, M = map(int, sys.stdin.readline().split())
sharks = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] # 0: x, 1: y (위치), 2: s(속력), 3: d(이동방향), 4: z(크기)
alive = [True]*M
sea = [[-1]*(C+1) for _ in range(R+1)]
for i in range(M):
    x, y = sharks[i][0], sharks[i][1]
    sea[x][y] = i

'''
1. 낚시왕이 오른쪽으로 한 칸 이동한다.
2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어((i, j)라고 할때 같은 j중 가장 작은 i인 상어)(O(200))를 잡는다. (alive인 상어 중에서)
3. 상어를 잡으면 격자판에서 잡은 상어가 사라진다. alive[상어번호] = False처리
4. 상어가 이동한다.
5. 같은 위치에 있는 상어는 가장 큰 상어 빼고 모두 alive = False 처리
'''
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
def get_shark(idx):
    score = 0
    for i in range(1, R+1):
        if sea[i][idx] != -1:
            alive[sea[i][idx]] = False
            score = sharks[sea[i][idx]][4]
            sea[i][idx] == 0 # 상어 없애기
            return score
    return score
            
            
    # min_shark = M+1
    # # sharks 뒤지기
    # for shark in range(M):
    #     if alive[shark] and sharks[shark][1] == idx:
    #         if min_shark == M+1: min_shark = shark # 처음 발견인 경우 업데이트를 해줘야함. 아웃오브인덱스 안나게
    #         else:
    #             if sharks[min_shark][0] > sharks[shark][0]: min_shark = shark
    # return min_shark
def move_step(x, y, s, d):
    global R, C
    while True:
        if d == 1 or d == 2: # 위, 아래. x만 움직임
            s = s % (2+(R-2)*2)
            nx = x + s*dx[d-1]
            if 1 < nx < R:
                return nx, y, d
            else:
                if d == 1: # 위
                    s -= (x - 1)
                    x = 1
                    d = 2
                else:
                    s -= (R - x)
                    x = R
                    d = 1
        else:
            s = s % (2+(C-2)*2)
            ny = y + s*dy[d-1]
            if 1 < ny < C:
                return x, ny, d
            else:
                if d == 4: # 왼쪽
                    s -= (y - 1)
                    y = 1
                    d = 3
                else:
                    s -= (C - y)
                    y = C
                    d = 4
        if s == 0: return x, y, d # 종료 조건
    
# 새출발하기
def move_shark():
    global R, C
    temp = [[-1]*(C+1) for _ in range(R+1)]
    for shark_idx in range(M):
        if not alive[shark_idx]: continue # 죽은 상어에 대해서는 하지 않음
        x, y = sharks[shark_idx][0], sharks[shark_idx][1] # 위치
        s = sharks[shark_idx][2] # 속도
        d = sharks[shark_idx][3] # 방향
        x, y, d = move_step(x, y, s, d)
        if temp[x][y] != -1:
            if sharks[temp[x][y]][4] < sharks[shark_idx][4]:
                alive[temp[x][y]] = False
                temp[x][y] = shark_idx
            else: alive[shark_idx] = False
        else: temp[x][y] = shark_idx
        # 바뀐 위치 업데이트
        sharks[shark_idx][0], sharks[shark_idx][1], sharks[shark_idx][3] = x, y, d
    # print(sharks)
    return temp
        
        
# def find(x, y, visited):
#     for idx in range(len(visited)):
#         if (x, y) == visited[idx]: return idx

# def eat_shark():
#     # 처음 shark 부터 좌표가 visited 리스트에 이미 있는 경우, 이미 있는 그 상어와 크기 비교
#     # 지금 상어가 더 큰 경우 리스트의 상어 크기와 상어 번호 바꿈 and 원래 있던 상어 죽음처리
#     visited_xy = []
#     visited_iz = []
#     for shark_idx in range(M):
#         if not alive[shark_idx]: continue
#         (x, y) = (sharks[shark_idx][0], sharks[shark_idx][1])
#         z = sharks[shark_idx][4]
#         if (x, y) in visited_xy:
#             idx = find(x, y, visited_xy)
#             (ii, zz) = visited_iz[idx]
#             if z > zz:
#                 # 지금 상어가 더 큰 경우 리스트의 상어 크기와 상어 번호 바꿈
#                 visited_iz[idx] = (shark_idx, z)
#                 # 원래 상어 죽음처리
#                 alive[ii] = False
#             else:
#                 alive[shark_idx] = False
#         else:
#             visited_xy.append((x, y))
#             visited_iz.append((shark_idx, z))
    

human = 0
score = 0
while True:
    human += 1 # 오른쪽으로 이동
    score += get_shark(human)
    # print(score)
    # shark_idx = get_shark(human) # 낚시
    # if shark_idx < M:
    #     alive[shark_idx] = False # 잡힌거임
    #     # 점수 추가
    #     score += sharks[shark_idx][4]
    # 상어 이동
    sea = move_shark()
    # eat_shark() # 같은 위치에 있는 상어 잡아먹기
    # print(sea)
    if human == C: break # 종료 조건

print(score)
# print(sharks)
# deepcopy 적게

## 딕셔너리 값 삭제: del dic[key] !!
## 얜 visited 확인 필요 없음. (순서 다르게 잡아먹으면 한번 먹고 물고기가 이동해서 같아질 수가 없음.)
## 상어의 eat을 반복문을 도는데 새로운 변수로 안할당해서 계속 값이 증가했음.
## 물고기가 방향을 바꿀때 리턴값을 안 저장했음.


'''
1. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 
2. 이후 물고기가 이동한다.
3. 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
    - 물고기는 한 칸을 이동할 수 있음.
    - 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
    - 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 
    - 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 
    - 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 
    - 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
4. 물고기의 이동이 모두 끝나면 상어가 이동한다. 
    - 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. (물고기가 있는 칸으로만 지나갈 수 있음)
    - 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 
    - 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다.
    - 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 
    - 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
'''
import sys
from collections import deque
from copy import deepcopy
visited = []
stack = deque()
# 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
max_eat = -1
osea = [[0]*4 for _ in range(4)]
# [번호, 방향]끼리 묶어서 리스트 생성
for j in range(4):
    li = list(map(int, sys.stdin.readline().split()))
    pair = []
    for i in range(8):
        pair.append(li[i])
        if i % 2 == 1:
            pair[1] -= 1
            osea[j][i//2] = pair
            pair = []
            
def rotate_fish(d):
    d = (d+1)%8
    return d

def can_go_fish(x, y, sea):
    if 0<=x<4 and 0<=y<4 and (sea[x][y] == 0 or sea[x][y][0] != -1): return True
    return False

def can_go_shark(x, y, sea):
    if 0<=x<4 and 0<=y<4 and sea[x][y] != 0: return True
    return False

def dfs():
    global max_eat
    while stack:
        (sea, x, y, eat) = stack.pop()
        # print(f'before eat: {eat}')
        # 물고기 움직이기
        for fish in range(1, 17):
            # 바다에서 물고기 순서대로 찾기
            found = False
            fx, fy = -1, -1
            for i in range(4):
                for j in range(4):
                    if sea[i][j] != 0 and sea[i][j][0] == fish:
                        found = True
                        fx, fy = i, j
                        break
                if found: break
            if found:
                fd = sea[fx][fy][1]
                for _ in range(8):
                    fnx, fny = fx + dx[fd], fy + dy[fd]
                    if not can_go_fish(fnx, fny, sea):
                        fd = rotate_fish(fd) # 방향바꿔서 다시 도전
                    else:
                        # 서로 위치 바꾸고 다음 물고기로 넘어가기
                        if sea[fnx][fny] == 0: sea[fx][fy] = 0
                        else:
                            sea[fx][fy] = sea[fnx][fny][:]
                        sea[fnx][fny] = [fish, fd]
                        break
        # print(sea)
        
        # 상어 움직이기
        moved = False
        d = sea[x][y][1]
        for i in range(1, 4):
            nsea = deepcopy(sea)
            neat = eat
            nx, ny = x + dx[d]*i, y + dy[d]*i
            if can_go_shark(nx, ny, nsea):
                moved = True
                neat += nsea[nx][ny][0]
                # print(neat)
                nsea[nx][ny][0] = -1
                nsea[x][y] = 0
                # 그리고 stack에 넣기. (not visited일때만) 
                # if (nx, ny, nsea) not in visited:
                    # 물고기 먹고 그 자리 차지.
                stack.append((deepcopy(nsea), nx, ny, neat))
                visited.append((nx, ny, deepcopy(nsea)))
    
        if not moved:
            # 최대 먹은 수 저장   
            max_eat = max(max_eat, eat)        

eat = osea[0][0][0]
osea[0][0][0] = -1
stack.append((deepcopy(osea), 0, 0, eat))
visited = []
# visited.append((0, 0, deepcopy(osea)))

dfs()

print(max_eat)
            
                    

## 깊은 복사 하려면 copy import 해서 copy.deepcopy(arr)!
## conv 범위. 반복문 범위.
# 1. 폴리오미노 리스트 만들기
    # 1. 5가지 모양의 폴리오미노 리스트 5개 생성
    # 2. 각 모양별로 회전 혹은 대칭 시켜서 만들 수 있는 서로다른 배열들 저장
# 2. 폴리오미노마다 주어진 board를 처음부터 돌면서 최대 합 저장.
from copy import deepcopy
import sys
poly_b = [[[1, 1, 1, 1]], [[1],[1],[1],[1]]] # 회전 1, 대칭 X
poly_y = [[[1, 1],      # 회전 X, 대칭 X
          [1, 1]]]
poly_o = [[[1, 0],      # 그대로 회전 3, 대칭 1 후 회전 3
          [1, 0],
          [1, 1]],]
poly_g = [[[1, 0],      # 그대로 회전 1, 대칭 1 후 회전 1
          [1, 1],
          [0, 1]]]
poly_p = [[[1, 1, 1],   # 회전 3, 대칭 X
          [0, 1, 0]]]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2차원 배열의 회전
# n*m: (0, 0)-(0, n-1) (0, 1)-(1, n-1), ...(0, n-1)-(m-1, n-1)
# (1, 0)-(0, n-1-1) (1, 1)-(1, n-1-1), ...

# 시계방향으로 90도 회전시키는 함수
def rotate(arr):
    n, m = len(arr), len(arr[0])
    new_arr = [[1]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                new_arr[j][n-1-i] = 0
    return new_arr

# (0,0)->()
# 세로축 대칭시키는 함수
def reflect(arr):
    n, m = len(arr), len(arr[0])
    new_arr = deepcopy(arr)
    for i in range(n):
        for j in range(m):
            # 행은 그대로, 열만 바뀜
            new_arr[i][m-1-j] = arr[i][j]
    return new_arr

def conv(i, j, poly):
    s = 0
    for k in range(i, i+len(poly)):
        for g in range(j, j+len(poly[0])):
            s += board[k][g]*poly[k-i][g-j]
    return s
    

def make():
    # 그대로 회전 3 (o, p)
    for _ in range(3):
        poly_o.append(rotate(poly_o[-1]))
        poly_p.append(rotate(poly_p[-1]))
        
    # 대칭 후 회전 3 (o)
    poly_o.append(reflect(poly_o[0]))
    for _ in range(3):
        poly_o.append(rotate(poly_o[-1]))
        
    # 그대로 회전 1, 대칭 1 후 회전 1 (g)
    poly_g.append(rotate(poly_g[-1]))
    poly_g.append(reflect(poly_g[0]))
    poly_g.append(rotate(poly_g[-1]))

make()

all_polies = []
all_polies.append(poly_b)
all_polies.append(poly_y)
all_polies.append(poly_o)
all_polies.append(poly_g)
all_polies.append(poly_p)

result = -sys.maxsize
for polies in all_polies:
    for poly in polies:
        for i in range(n-len(poly)+1):
            for j in range(m-len(poly[0])+1):
                result = max(result, conv(i, j, poly))
print(result)



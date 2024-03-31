
### 주사위 그려보면서 다시 해보기
'''
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
'''
import sys

'''
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
'''

(N, M, x, y, comm_len) = tuple(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int, sys.stdin.readline().split()))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 동 서 북 남
dice = {i:0 for i in range(1, 7)}
downside = {2: 5, 4: 3, 1: 6, 6: 1, 5: 2, 3: 4} # key가 윗면, value가 반대편 면(바닥면)
shape_of_dice = [ 
                   [2],
                [4, 1, 3],
                   [5],
                   [6]
                ]
# 윗면은 항상 1,1
def roll_dice(c, shape_of_dice):
    # 동쪽이면 1행의 i번째를 (i+1)%3위치로 다 바꿈
    # 서쪽이면 1행의 i번째를 (i-1)%3위치로 다 바꿈
    if c == 1 or c == 2:
        m = 1 if c == 1 else -1
        two_zero = 2 if c == 1 else 0
        new = [0, 0, 0]
        for j in range(3):
            if j == two_zero:
                new[2-j] = shape_of_dice[3][0]
                shape_of_dice[3][0] = shape_of_dice[1][j]
            else:
                new_j = (j+m)%3
                new[new_j] = shape_of_dice[1][j]
            
        shape_of_dice[1] = new
    
    # 북쪽이면 1행은 1열, 나머지는 0열들의 i행을 (i-1)%4로 바꿈. 이때 2행은 1행의 *1*로 바뀌는점 주의
    # 남쪽이면 1행은 1열, 나머지는 0열들의 i행을 (i+1)%4로 바꿈. 이때 0행은 1행의 *1*로 바뀌는점 주의
    if c == 3 or c == 4:
        old_shape_of_dice = [sod[:] for sod in shape_of_dice]
        m = -1 if c == 3 else 1
        two_zero = 2 if c == 3 else 0
        for i in range(4):
            new_i = (i+m)%4
            # print(new_i, i)
            if i != two_zero and i != 1:
                shape_of_dice[new_i][0] = old_shape_of_dice[i][0]
            elif i == two_zero: shape_of_dice[new_i][1] = old_shape_of_dice[i][0]
            elif i == 1: shape_of_dice[new_i][0] = old_shape_of_dice[i][1]

def in_range(x, y):
    if 0<=x<N and 0<=y<M: return True
    return False

# 주사위는 처음에 바닥면이 6인 상태로 시작. 초기 상태 주사위는 모두 0임
dice[6] = board[x][y]
if board[x][y] != 0: board[x][y] = 0
guide = 1
for c in commands:
    # 좌표 업데이트
    nx, ny = x + dx[c-1], y + dy[c-1]
    if in_range(nx, ny): 
        x, y = nx, ny
        # 주사위 굴리기
        roll_dice(c, shape_of_dice)
        # print(shape_of_dice)
        # 바닥 면에 있는 수 칸에 복사
        if board[x][y] == 0: 
            board[x][y] = dice[downside[shape_of_dice[1][1]]]
        # 칸에 쓰여진 수가 0이 아니라면 주사위의 바닥면에 칸의 수 복사
        else: 
            dice[downside[shape_of_dice[1][1]]] = board[x][y]
            board[x][y] = 0
        # print(shape_of_dice)
        # print(f'dice: {dice}')
        # 윗면 수 출력
        print(dice[shape_of_dice[1][1]])
        
    
    
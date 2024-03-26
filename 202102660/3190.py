'''
게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
rotation = {}
for _ in range(l):
    x, c = sys.stdin.readline().split()
    rotation[int(x)] = c
time = 0
snake_head = (1, 1)

snake = deque()
snake.append(snake_head)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오, 아, 왼, 위 -> 시계방향
d = 0 # 오른쪽을 보고 시작.

def rotate(c, d):
    # 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
    if c == 'L': d = (d - 1)%4
    else: d = (d + 1)%4
    return d
    

def crash(snake):
    (x, y) = snake.popleft()
    if not in_board(x, y) or (x, y) in snake: return True
    snake.appendleft((x, y))
    return False

def in_board(x, y):
    if 1<= x <= n and 1<= y <= n: return True
    return False
    

def move_head(snake, d):
    head = snake[0]
    x, y = head[0] + dx[d], head[1] + dy[d]
    snake.appendleft((x, y))
    
    
def move_tail(snake):
    snake.pop()
    

while True:
    time += 1
    # 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    move_head(snake, d)
    
    # 2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if crash(snake): break
    
    # 3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if snake[0] in apples:
        apples.remove(snake[0])
        
    # 4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        move_tail(snake)
    
    # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
    if time in rotation.keys():
        c = rotation[time]
        d = rotate(c, d)

print(time)
        
        
    
    


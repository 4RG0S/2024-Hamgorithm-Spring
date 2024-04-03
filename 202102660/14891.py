## 바로 양 옆 바퀴만 움직이고, 그 바퀴가 움직이면서 그 바퀴의 이웃바퀴들도 움직인다는 것을 잊음!
## 명령의 해당 인덱스 바퀴를 움직이는 걸 까먹음! (안움직이고 이웃바퀴만 움직임)
## save_point해야하는 이유

'''
첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. 
N극은 0, S극은 1로 나타나있다.

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 
다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
'''
import sys
from collections import deque
n = 4
wheels = [deque(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
K = int(sys.stdin.readline())
instr = [tuple((map(int, sys.stdin.readline().split()))) for _ in range(K)]
que = deque()
saved = []
def rotate(wheel_idx, d):
    wheel = wheels[wheel_idx]
    if d == 1:
        w = wheel.pop()
        wheel.appendleft(w)
    else:
        w = wheel.popleft()
        wheel.append(w)

def save_point():
    global saved
    saved = [[wheel[2], wheel[6]] for wheel in wheels]
    # return saved 

def spread():
    while que:
        (wheel_idx, d, to_go) = que.popleft()
        
        if to_go == "left":
            if wheel_idx - 1 >= 0:
                if saved[wheel_idx-1][0] != saved[wheel_idx][1]:
                    rotate(wheel_idx-1, -d)
                    que.append((wheel_idx-1, -d, "left"))
        else: 
            if wheel_idx + 1 <= 3:
                if saved[wheel_idx+1][1] != saved[wheel_idx][0]:
                    rotate(wheel_idx+1, -d)
                    que.append((wheel_idx+1, -d, "right"))
                          
for (num, d) in instr:
    save_point()
    # 각 번호-1: wheel에 해당하는 인덱스
    # 각 번호의 6번인덱스 왼쪽(-1)은 2번 인덱스, 번호의 2번인덱스 오른쪽(+1)은 6번 인덱스 확인
    # 극이 다른 경우: 회전하는 함수호출(이때 매개변수로 -방향 값 넘겨주기)
    wheel_idx = num -1
    ## 이걸 까먹음!!
    rotate(wheel_idx, d)
    # 왼쪽거 확인
    if wheel_idx - 1 >= 0:
        if saved[wheel_idx-1][0] != saved[wheel_idx][1]:
            rotate(wheel_idx-1, -d)
            que.append((wheel_idx-1, -d, "left"))
    # 오른쪽거 확인
    if wheel_idx + 1 <= 3:
        if saved[wheel_idx+1][1] != saved[wheel_idx][0]:
            rotate(wheel_idx+1, -d)
            que.append((wheel_idx+1, -d, "right"))
    spread()
    
'''
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''
score =  0

for i in range(4):
    if wheels[i][0] == 1:
        score += 2**i
print(score)      
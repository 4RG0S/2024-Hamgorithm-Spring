# 배열을 처음부터 돌면서 모든 조합에 대해 최대이익 구하기
# 약간 dfs 비슷함. a를 상담할때 할 수 있는 상담 b, c, d를 가까운 순으로 스택에 넣고 (가격과 같이 넣기)
    # 상담할 수 있는 기준: 날짜에 상담 시 걸리는 날짜 더했을때 N 넘어가면 안됨, 기준 상담이 끝나고 할 수 있는 날짜.
# 스택에 담긴 것을 빼면서 또 위 과정을 반복

import sys
from collections import deque

N = int(sys.stdin.readline())
schedule = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

stack = deque()
max_pay = 0

def can_meeting(prev, now, day):
    # prev: 직전 상담이 끝나는 날짜
    # 직전 상담과 겹치지 않는지
    # 이 상담을 해도 N을 넘지 않는지
    if prev < now and now+(day-1) <= N-1:
        return True
    return False
 
for (i, (day, pay)) in enumerate(schedule):
    if can_meeting(-1, i, day):
        end = i + day-1 ## 여기서 i를 안 더해서 틀렸었음!!
        stack.append((pay, i, end))

def dfs():
    global max_pay
    while stack:
        (pay, i, prev) = stack.pop()
        add_meet = False
        for idx in range(i+1, N):
            day = schedule[idx][0]
            idx_pay = schedule[idx][1]
            if can_meeting(prev, idx, day):
                end = idx + day - 1
                stack.append((pay+idx_pay, idx, end))
                add_meet = True
        if not add_meet:
            max_pay = max(max_pay, pay)

dfs()
print(max_pay)
                

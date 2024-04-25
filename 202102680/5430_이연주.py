import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()     # 수행할 함수 p
    p = p[0:-1]     # 입력 맨 뒤 \n 제거
    n = int(input())    # 배열에 들어 있는 수 n
    arr = input()    #
    dq = deque(arr[1:-2].split(","))
    check = 1   # deque 출력 할 지 말 지
    count = 0   # R의 개수
    if n == 0:  # 배열 안에 아무 것도 없다고 하면? arr
        dq = deque()
    for i in p:     # 함수 하나씩 읽기
        if i == "R":    # R이면? count +=1
            count += 1
        elif i == "D":  # D이면?
            if len(dq) == 0:   # 지울 게 없을 때 error 출력
                print("error")
                check = 0   # deque 출력 안해도 됨. error 출력 하니까
                break
            if count % 2 == 0:
                dq.popleft()
            else:
                dq.pop()

    if check != 0:
        if count % 2 == 0:
            print("["+",".join(dq)+"]")
        else:
            dq.reverse()
            print("["+",".join(dq)+"]")

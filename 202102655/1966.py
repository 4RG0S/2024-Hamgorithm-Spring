from collections import deque

test_cnt = int(input())

for _ in range(test_cnt):
    N, M = map(int, input().split())
    get_idx = M
    importance = deque(map(int, input().split()))
    cnt = 0
    while (True):    
        get_importance = importance.popleft()
        if len(importance) == 0:
            print(cnt + 1)
            break
        if get_importance < max(importance):
            if get_idx == 0:
                get_idx += len(importance)
            else:
                get_idx -= 1
            importance.append(get_importance)
        else:
            cnt += 1
            if get_idx == 0:
                print(cnt)
                break
            get_idx -= 1
    
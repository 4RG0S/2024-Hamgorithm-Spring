from collections import deque

n, m = map(int, input().split())
rotate_queue = deque([i for i in range(1, n+1)])

nums = list(map(int, input().split()))

cnt = 0
current = 0
for num in nums:
    while True:
        if rotate_queue[0] == num:
            rotate_queue.popleft()
            break
        else:
            if rotate_queue.index(num) <= (len(rotate_queue) // 2):  
                rotate_queue.rotate(-1)
                cnt += 1
            else:
                rotate_queue.rotate(1)
                cnt += 1
print(cnt)
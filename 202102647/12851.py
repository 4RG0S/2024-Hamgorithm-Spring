import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
dist = [0] * 100001

def BFS(n):
    result = 0
    count = 0
    que = deque([n])
    while que:
        a = que.popleft()
        if a == k:
            result = dist[a]    
            count += 1
            continue
        for next in (a + 1, a - 1, 2*a):
            if 0<= next <= 100000 and (not dist[next] or dist[next] - dist[a] ==  1):
                dist[next] = dist[a] + 1
                que.append(next)
    print(result)
    print(count)
BFS(n)

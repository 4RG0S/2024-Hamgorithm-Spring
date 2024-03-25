import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())

result = [0] * 100001

def BFS(n):
    que = deque([n]) 
    while que:
        a = que.popleft()
        if a == k :
            print(result[a])
            break
        for next in (a-1, a+1, 2*a):
            if 0<=next<100001 and not result[next]:
                result[next] = result[a] + 1
                que.append(next)
                
BFS(n)
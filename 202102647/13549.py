import sys
from collections import deque
n,k= map(int,sys.stdin.readline().split())
graph = [-1] * 100001

def bfs(n):
    graph[n]= 0
    que = deque([n])
    while que:
        a = que.popleft()
        if a==k:
            print(graph[a])
            return
        for next in (a-1,a+1,2*a):
            if 0<=next<100001 and graph[next] == -1:
                if next == 2*a:
                    graph[next] = graph[a]
                    que.appendleft(next)
                else:
                    graph[next] = graph[a] + 1
                    que.append(next)

bfs(n)
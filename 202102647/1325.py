import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for i in range (n+1)]

def bfs(k):
    que = deque([k])
    count = 1
    visited = [0] * (n+1)
    visited[k]=True
    while(que):
        a = que.popleft()
        for next in graph[a]:
            if not visited[next]:
                visited[next] = 1 
                que.append(next)
                count+=1
    return count

for i in range (m):
    a,b =map(int,sys.stdin.readline().split())
    graph[b].append(a)

answer = []
for i in range (1,n+1):
    answer.append(bfs(i))
maxValue = max(answer)
for i in range (len(answer)):
    if maxValue == answer[i]:
        print(i+1, end= ' ')


import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
graph = [0] * 100001
arr = [0] * 100001
def count(x):
    data = []
    temp = x
    for _ in range(graph[x]+1):
        data.append(temp)
        temp = arr[temp]
    print(' '.join(map(str, data[::-1])))
def bfs(n):
    que = deque([n])
    while(que):
        # print(que)
        a = que.popleft()
        if a == k:
            # print(que)
            print(graph[a])
            count(a)
            break
        for next in (a - 1, a+1, 2*a):
            if 0<=next<100001 and not graph[next]:
                graph[next] = graph[a]+1
                que.append(next)
                arr[next] = a


bfs(n)
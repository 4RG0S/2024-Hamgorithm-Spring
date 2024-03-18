import sys
from collections import deque, defaultdict

N, Q = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(N-1) :
    p, q, r = list(map(int, input().split()))
    graph[p].append((q, r))
    graph[q].append((p, r))

for j in range(Q):
    count = 0
    k, v = list(map(int, input().split()))
    queue = deque([(v, float('inf'))])
    visit = [False for _ in range(N+1)]
    while queue:
        dot, usado = queue.popleft()
        visit[dot] = True
        for link, u in graph[dot]:
            min_u = min(u,usado)
            if visit[link]==False and min_u >= k:
                count+=1
                queue.append((link, min_u))
    print(count)







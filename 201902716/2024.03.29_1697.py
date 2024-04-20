import sys
from collections import deque

X, K = map(int, sys.stdin.readline().split())


def bfs(X, K):
    visited = [False] * 100001
    queue = deque([(X, 0)])
    visited[X] = True

    while queue:
        cur_x, t = queue.popleft()
        if cur_x == K:
            return t
        for next_x in (cur_x - 1, cur_x + 1, cur_x * 2):
            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = True
                queue.append((next_x, t + 1))


print(bfs(X, K))

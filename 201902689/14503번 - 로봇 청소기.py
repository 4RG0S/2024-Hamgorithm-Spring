import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 0 = 북, 1 = 동, 2 = 남, 3 = 서
# 청소 순서는 북 -> 서 -> 남 -> 동 순서다. 0 -> 3 -> 2 -> 1
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
is_cleaned = [[False for _ in range(m)] for _ in range(n)]
def check(r, c):
    return 0 <= r < n and 0 <= c < m

def vaccum(r, c, d):
    count = 0
    queue = deque()
    queue.append((r, c, d))
    while queue:
        r, c, d = queue.popleft()
        # 청소해야 하면 청소
        if not is_cleaned[r][c]:
            is_cleaned[r][c] = True
            count += 1
        # 청소 할 곳 확인
        is_find = False
        nd = d
        for _ in range(4):
            nd = (nd + 3) % 4
            nr, nc = r + directions[nd][0], c + directions[nd][1]
            if check(nr, nc) and graph[nr][nc] == 0:
                if not is_cleaned[nr][nc]:
                    queue.append((nr, nc, nd))
                    is_find = True
                    break
        if not is_find:
            nr, nc = r - directions[d][0], c - directions[d][1]
            if check(nr, nc) and graph[nr][nc] == 0:
                queue.append((nr, nc, d))
            else:
                return count

result = vaccum(r, c, d)
print(result)

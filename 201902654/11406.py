from collections import deque

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
paths = [[0 for _ in range(len(A) + len(B) + 2)] for _ in range(len(A) + len(B) + 2)]
# 0: start, 1 ~ len(B): 서점 book, len(B) + 1, len(A) + len(B): 사람 book, len(A) + len(B) + 1: end
for i in range(M):
  book = B[i]
  paths[0][i + 1] = book
for i in range(M):
  limits = list(map(int, input().split()))
  for j in range(len(limits)):
    limit = limits[j]
    paths[i + 1][1 + M + j] = limit
for i in range(N):
  limit = A[i]
  paths[1 + M + i][1 + M + N] = limit

while True:
  # dest, paths, min
  queue = deque()
  is_visit = [False for _ in range(2 + M + N)]
  queue.append([0, [0], float('inf')])
  is_visit[0] = True
  shortest_path = []
  while len(queue) != 0:
    dest, path, minimum = queue.popleft()
    for i in range(len(paths[dest])):
      if paths[dest][i] > 0 and is_visit[i] == False:
        is_visit[i] = True
        next_path = path + [i]
        next_minimum = min(minimum, paths[dest][i])
        queue.append([i, next_path, next_minimum])
        if i == 1 + M + N:
          shortest_path = [next_path, next_minimum]
          queue = []
  if len(shortest_path) == 0:
    break
  path, minimum = shortest_path
  for i in range(len(path) - 1):
    paths[path[i]][path[i + 1]] -= minimum
    paths[path[i + 1]][path[i]] += minimum

result = 0
for val in paths[1 + M + N]:
  result += val

print(result)

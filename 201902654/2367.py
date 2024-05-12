import sys
from collections import deque

N, K, D = list(map(int, sys.stdin.readline().split()))
paths = [[0 for _ in range(D + N + 2)] for _ in range(D + N + 2)]
line = list(map(int, sys.stdin.readline().split()))
# 0: start, 1 ~ D: foods, D + 1 ~ D + N: people, D + N + 1: end
for i in range(D):
  paths[0][i + 1] = line[i]
for i in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  z = line[0]
  for j in range(z):
    paths[line[j + 1]][i + D + 1] = 1
for i in range(N):
  paths[D + i + 1][D + N + 1] = K

while True:
  # [dest, paths, min]
  queue = deque()
  queue.append([0, [0], float('inf')])
  final_paths = []
  is_visit = [False for _ in range(D + N + 2)]
  is_visit[0] = True
  while len(queue) != 0:
    dest, path, minimum = queue.popleft()
    for i in range(len(paths[dest])):
      if paths[dest][i] > 0:
        to = i
        val = paths[dest][i]
        if is_visit[to] != True:
          is_visit[to] = True
          next_path = path + [to]
          minimum_value = min(minimum, val)
          queue.append([to, next_path, minimum_value])
          if to == D + N + 1:
            final_paths.append([next_path, minimum_value])
            queue = []

  if len(final_paths) == 0:
    break

  for path in final_paths:
    p, v = path
    for i in range(len(p) - 1):
      paths[p[i]][p[i + 1]] -= v
      paths[p[i + 1]][p[i]] += v

# for path in paths:
#   print(path)
result = 0
for val in paths[D + N + 1]:
    result += val
print(result)

# print(paths[D + i + 1])

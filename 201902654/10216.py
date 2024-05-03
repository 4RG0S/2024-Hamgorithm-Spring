import sys

T = int(sys.stdin.readline())
global parents
parents = []

def get_parent(x):
  global parents
  if parents[x] == x:
    return x
  return get_parent(parents[x])

def union_parent(a, b):
  global parents
  a = get_parent(a)
  b = get_parent(b)
  if a < b:
    parents[b] = a
  else:
    parents[a] = b

for _ in range(T):
  N = int(sys.stdin.readline())
  parents = [i for i in range(N)]
  enemies = []
  for _ in range(N):
    x, y, R = list(map(int, sys.stdin.readline().split()))
    enemies.append((x, y, R))
  for i in range(N):
    for j in range(i + 1, N):
      x1, y1, R1 = enemies[i]
      x2, y2, R2 = enemies[j]
      if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (R1 + R2) ** 2:
        union_parent(i, j)
  count = 0
  for i in range(N):
    if get_parent(i) == i:
      count += 1
  print(count)

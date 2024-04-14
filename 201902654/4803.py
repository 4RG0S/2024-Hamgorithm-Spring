import sys

def get_parent(x):
  global parents
  if parents[x] == x:
    return x
  return get_parent(parents[x])

def union_parent(a, b):
  global parents, count
  a = get_parent(a)
  b = get_parent(b)
  if a < b:
    parents[b] = a
    count[a] += count[b]
  else:
    parents[a] = b
    count[b] += count[a]

global parents, count
case = 0
while True:
  case += 1
  N, M = list(map(int, sys.stdin.readline().split()))
  if N == 0 and M == 0:
    break
  parents = [i for i in range(N)]
  count = [1 for _ in range(N)]
  for _ in range(M):
    parent, child = list(map(int, sys.stdin.readline().split()))
    union_parent(parent - 1, child - 1)
  for i in range(N):
    count[get_parent(i)] -= 1
  count = (count.count(0))
  print("Case " + str(case) + ": ", end="")
  print("No trees." if count == 0 else "There is one tree." if count == 1  else "A forest of " + str(count) + " trees.")

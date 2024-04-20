import sys


N = int(sys.stdin.readline())
global parents
parents = [i for i in range(N)]

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

for _ in range(N - 2):
  parent, child = list(map(int, sys.stdin.readline().split()))
  union_parent(parent - 1, child - 1)


compare = get_parent(0)
result = [compare]
for i in range(N):
  if compare != get_parent(i):
    result.append(get_parent(i))
    break

print(result[0] + 1, result[1] + 1)

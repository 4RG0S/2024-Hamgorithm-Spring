import sys

T = int(sys.stdin.readline())
global parents
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
for i in range(T):
  N = int(sys.stdin.readline())
  K = int(sys.stdin.readline())
  parents = [i for i in range(N)]
  for _ in range(K):
    parent, child = list(map(int, sys.stdin.readline().split()))
    union_parent(parent - 1, child - 1)

  M = int(sys.stdin.readline())
  sys.stdout.write("Scenario " + str(i + 1) + ":\n")
  for _ in range(M):
    parent, child = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(str(1 if get_parent(parent - 1) == get_parent(child - 1) else 0) + "\n")
  sys.stdout.write("\n")

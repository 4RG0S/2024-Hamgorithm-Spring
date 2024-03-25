import sys

N, K = map(int, sys.stdin.readline().split())

p = list(x for x in range(1, N + 1))
result = []
IDX = 0
while p:
    IDX += K - 1
    if IDX >= len(p):
        IDX %= len(p)
    tmp = p.pop(IDX)
    result.append(tmp)
  
print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')

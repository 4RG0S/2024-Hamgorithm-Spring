import sys

N = int(sys.stdin.readline())
data = list()
for _ in range(N):
    data.append(int(sys.stdin.readline()))

print('\n'.join(map(str, sorted(data))))

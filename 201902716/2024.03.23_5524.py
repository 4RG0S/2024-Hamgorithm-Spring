import sys

N = int(sys.stdin.readline())
names = [sys.stdin.readline().rstrip().lower() for _ in range(N)]

for name in names:
    print(name)

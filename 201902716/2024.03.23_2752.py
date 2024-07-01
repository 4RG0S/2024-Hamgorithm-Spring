import sys

data = list(map(int, sys.stdin.readline().split()))
data.sort()

print(*data)

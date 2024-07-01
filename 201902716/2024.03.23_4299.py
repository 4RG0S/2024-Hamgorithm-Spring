import sys

sum, sub = map(int, sys.stdin.readline().split())

a = (sum + sub) // 2
b = sum - a

if b < 0 or (sum + sub) % 2 != 0:
    print(-1)
else:
    print(max(a, b), min(a, b))

import sys

num = list(map(int, sys.stdin.readline().strip().split(' ')))

s = min(num)
while True:
    res = 0
    for i in num:
        if s % i == 0:
            res += 1
    if res >= 3:
        break
    s += 1

print(s)

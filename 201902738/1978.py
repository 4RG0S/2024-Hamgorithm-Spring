import sys

T = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

res = T

for i in range(0, T):
    n = data[i]
    if n > 1:
        check = True
        for j in range(2, n):
            if n % j == 0:
                check = False
                break
        if not check:
            res -= 1
    else:
        res -= 1

print(res)

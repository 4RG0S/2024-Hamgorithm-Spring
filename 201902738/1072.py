import sys

X, Y = map(int, sys.stdin.readline().split())

rate = int((Y * 100) / X)
start = 1
end = 10 ** 9 + X


change = False
cnt = 0
while start <= end:
    mid = (start + end) // 2
    if int((Y+mid) * 100/(X+mid)) > rate:
        change = True
        end = mid - 1
    else:
        start = mid + 1

print(start if change else -1)

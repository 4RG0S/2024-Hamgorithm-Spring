import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
start, end = 0, n-1
check = sys.maxsize

while start < end:
    cal = arr[start] + arr[end]
    if abs(cal) < check:
        check = abs(cal)
        ans = [arr[start], arr[end]]
    if cal < 0:
        start += 1
    elif cal > 0:
        end -= 1
    else:
        break

print(ans[0],ans[1])

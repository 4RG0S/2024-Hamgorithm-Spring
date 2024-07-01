import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1

result = 2000000001
left, right = 0, 0

while start != end:
    summation = abs(arr[start] + arr[end])
    if summation <= result:
        left, right = arr[start], arr[end]
        result = summation
    if arr[start] + arr[end] < 0:
        start += 1
    elif arr[start] + arr[end] > 0:
        end -= 1
    else:
        print(arr[start], arr[end])
        exit(0)

print(left, right)
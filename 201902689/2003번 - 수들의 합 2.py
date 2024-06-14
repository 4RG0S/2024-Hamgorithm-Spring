import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

def two_pointer(n, m, arr):
    start, end = 0, 0
    count = 0
    # summation = arr[start]
    summation = 0
    for i in range(n):
        while summation < m and end < n:
            summation += arr[end]
            end += 1
        if summation == m:
            count += 1
        summation -= arr[i]
    print(count)

def solution2(n, m, arr):
    start, end = 0, 0
    count = 0
    summation = 0
    while True:
        # 조건문의 순서도 중요함. summation < m 조건을 먼저 주면 out of index 에러 발생가능
        if summation == m:
            count += 1
            summation -= arr[start]
            start += 1
        elif summation > m:
            summation -= arr[start]
            start += 1
        elif end == n:
            break
        elif summation < m:
            summation += arr[end]
            end += 1
    print(count)

# two_pointer(n, m, arr)
solution2(n, m, arr)
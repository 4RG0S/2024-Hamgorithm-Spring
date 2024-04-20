import sys
input = sys.stdin.readline
arr = [[0, 0]]
n, k = map(int, input().split())
d = [[0 for _ in range(k + 1)] for _ in range(n + 1)] 

for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = arr[i][0], arr[i][1]
        if j < weight:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-weight] + value)

result = d[n][k]
print(result)
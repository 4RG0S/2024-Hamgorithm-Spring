import sys

num = int(sys.stdin.readline())
Array = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(num)]



for i in range(num):
    for j in range(i):
        if Array[i] > Array[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))

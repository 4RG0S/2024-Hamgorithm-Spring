import math
import sys
a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range (a)]
dp[0] = arr[0]
maxValue = dp[0]
for i in range (1,a):
    dp[i] = max(dp[i-1]+arr[i],arr[i])
    maxValue = max(dp[i], maxValue)
print(maxValue)


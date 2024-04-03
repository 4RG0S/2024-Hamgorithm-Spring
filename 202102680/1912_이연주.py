import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [0] * n
dp[0] = arr[0]
ans = max(-sys.maxsize,dp[0])
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    if ans < dp[i]:
        ans = dp[i]

print(ans)
import sys
N = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
if N ==1:
    print(1)
elif N == 2:
    print(2)
else:
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % 10007)
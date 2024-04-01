import sys

T = int(sys.stdin.readline().rstrip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])

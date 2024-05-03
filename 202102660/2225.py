## 순서는 앞의 경우에서 다 고려함!! 다시 풀어보기
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
# 순서 다른 경우 다른 경우로 취급

import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[1]*(N+1) for _ in range(K+1)]
# dp[k][n]: k개의 정수를 더해서 n이 되는 경우의 수
# = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n]
# = dp[k][n-1] + dp[k-1][n]
for i in range(2, K+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K][N]%1000000000)
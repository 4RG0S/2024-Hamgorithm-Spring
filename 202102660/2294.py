## coin이랑 dp의 index를 맞추는 것이 중요하다!!!
# 사용한 최소 동전 개수 구하기
# v(i, k) = min(v(i-1, k), v(i, k-coin[i])+1) : i번째 동전까지 사용하여 k원을 만드는 최소 동전 개수

import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, k+1):
    dp[0][i] = 10001

for i in range(1, n+1):
    dp[i][0] = 0
    for j in range(1, k+1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-coin[i-1]]+1) if j-coin[i-1] >= 0 else dp[i-1][j]

print(dp[n][k] if dp[n][k] != 10001 else -1)
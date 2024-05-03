## 메모리 초과!
# n가지의 가치가 다른 동전으로 k원을 만들 수 있는 경우의 수를 구하는 문제
# v(i, k) = v(i-1, k) + v(i, k-coin[i]) : i번째 동전까지 사용하여 k원을 만드는 경우의 수

import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

# dp = [[0]*(k+1) for _ in range(n+1)]
# dp[0][0] = 1
# for i in range(1, n+1):
#     dp[i][0] = 1
#     for j in range(1, k+1):
#         dp[i][j] = dp[i-1][j] + dp[i][j-coin[i-1]] if j-coin[i-1] >= 0 else dp[i-1][j]
    
# print(dp[n][k])

dp = [0]*(k+1) # dp[k] : k원을 만드는 경우의 수
dp[0] = 1
for i in range(n):
    # coin[i]까지 사용하여 k원을 만드는 경우의 수
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]
        
print(dp[k])
# 다시 풀기
import sys

N, K = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
items.sort(key=lambda x: x[0])

dp = [0] * (K+1) # i무게까지 담을 수 있는 최대 가치

for i in range(N):
    for j in range(K, 0, -1):
        if items[i][0] <= j:
            dp[j] = max(dp[j], dp[j-items[i][0]] + items[i][1])

print(dp[K])

import sys

N, K = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N)

for i in range(N):
    dp[i] = items[i][1]
    for j in range(N):
        
# 수식 완성하기 dp
# 꼭 다시 풀어보기
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(N-1)]

for i in range(N-1):
    if i == 0:
        dp[0][nums[i]] = 1
    else:
        for j in range(21):
            if dp[i-1][j] != 0:
                if 0 <= j + nums[i] <= 20:
                    dp[i][j+nums[i]] += dp[i-1][j]
                if 0 <= j - nums[i] <= 20:
                    dp[i][j-nums[i]] += dp[i-1][j]
print(dp[-1][nums[-1]])
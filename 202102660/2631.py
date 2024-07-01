# 번호를 순서대로 배치하기 위해 옮겨야하는 최소 횟수

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

dp = [1] * N # i번째 원소까지 증가하는 부분 수열의 최대 길이 (i번째 원소를 포함하는 경우)

for i in range(N):
    for j in range(i-1, -1, -1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))
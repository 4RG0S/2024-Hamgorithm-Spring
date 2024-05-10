# 줄이 겹치는 경우: 
    # A의 값이 더 크고 B의 값이 더 작은 경우
    # A의 값이 더 작고 B의 값이 더 큰 경우
    
# 돌면서 겹치는가 확인
# 안겹치면 이전 값 + 1


import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])

# 가장 긴 증가하는 부분 수열
dp = [0] * N # i번째 원소까지 증가하는 부분 수열의 최대 길이 (i번째 원소를 포함하는 경우)

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

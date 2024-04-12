import sys
N = int(sys.stdin.readline())
origin = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    origin[i] = int(sys.stdin.readline())

# init
if N> 3:
    dp[1] = origin[1]
    dp[2] = origin[1] + origin[2]
    dp[3] = max(origin[1] + origin[3], origin[2]+origin[3])
    for n in range(4, N+1):
        dp[n] = max(origin[n]+origin[n-1]+dp[n-3], origin[n]+dp[n-2])
elif N ==3:
    dp[1] = origin[1]
    dp[2] = origin[1] + origin[2]
    dp[3] = max(origin[1] + origin[3], origin[2] + origin[3])
elif N ==2:
    dp[1] = origin[1]
    dp[2] = origin[1] + origin[2]
else:
    dp[1] = origin[1]
print(dp[N])
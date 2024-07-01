# M가지 동전으로 N원을 만드는 방법의 수를 구하는 문제
# 동전의 가치가 주어질 때, 각 동전의 가치는 모두 다르다.
# 동전의 가치가 주어지면, 그 가치의 동전을 사용해서 N원을 만드는 방법의 수를 구해야 한다.
# dp[i] = i원을 만드는 방법의 수
# dp[i] = dp[i] + dp[i-coin]

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    N = int(sys.stdin.readline())
    
    dp = [0]*(N+1)
    dp[0] = 1
    
    # 입력받은 모든 동전에 대해
    for coin in coins:
        # coin원부터 N원까지
        for i in range(coin, N+1):
            dp[i] += dp[i-coin]
    
    print(dp[N])
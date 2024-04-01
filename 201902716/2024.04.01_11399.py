import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * 1001
people = list(map(int, sys.stdin.readline().split()))

people.sort()

dp[1] = people[0]
for i in range(2, len(people) + 1):
    dp[i] = dp[i - 1] + people[i - 1]

print(sum(dp))

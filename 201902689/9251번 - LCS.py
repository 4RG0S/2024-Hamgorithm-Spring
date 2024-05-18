import sys
input = sys.stdin.readline

str1 = input()
str2 = input()

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for _ in range(len2)] for _ in range(len1)]

    for i in range(1, len1):
        for j in range(1, len2):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    result = 0
    for i in range(len1):
        result = max(result, max(dp[i]))
    print(result)

lcs(str1, str2)
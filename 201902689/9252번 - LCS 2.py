import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    result = dp[len1][len2]
    subsequence = []

    i = len1
    j = len2
    while i > 0 and j > 0:
        now = dp[i][j]
        left = dp[i][j-1]
        up = dp[i-1][j]
        if now == up:
            i -= 1
        elif now == left:
            j -= 1
        else:
            subsequence.append(str1[i-1])
            i -= 1
            j -= 1
    subsequence.reverse()
    print(result)
    print("".join(subsequence))
lcs(str1, str2)
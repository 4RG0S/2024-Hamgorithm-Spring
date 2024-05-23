# 14888번 - 연산자 끼워넣기

n = int(input())

nums = list(map(int, input().split()))
plus, minus, mul, idv = map(int, input().split())

max_result = -1e9
min_result = 1e9

def dfs(i, result, plus, minus, mul, idv):
    global max_result, min_result

    if i == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if plus>0:
        dfs(i+1, result+nums[i], plus-1, minus, mul, idv)
    if minus > 0:
        dfs(i+1, result-nums[i], plus, minus-1, mul, idv)
    if mul > 0:
        dfs(i+1, result*nums[i], plus, minus, mul-1, idv)
    if idv>0:
        dfs(i+1, int(result/nums[i]), plus, minus, mul, idv-1)

dfs(1, nums[0], plus, minus, mul, idv)
print(int(max_result))
print(int(min_result))


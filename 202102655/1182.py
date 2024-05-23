# 1182번 - 부분수열의 합

n, s = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(idx, sum):  
    global cnt
    if idx == n:
        return
    if sum + nums[idx] == s:
        cnt += 1
    dfs(idx+1, sum+nums[idx])
    dfs(idx+1, sum)

cnt = 0
dfs(0, 0)
print(cnt)

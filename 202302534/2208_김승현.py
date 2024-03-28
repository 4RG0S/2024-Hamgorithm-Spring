import sys
input =sys.stdin.readline

n, m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
prefix = [0]*(n+1)
min_ = [0] * (n+1)
max_ = [0] * (n+1)
for i in range(n):
    prefix[i+1] = prefix[i]+arr[i]
min_[1] = prefix[1]
max_[n] = prefix[n]
for i in range(2,n+1):
    min_[i] = min(min_[i-1],prefix[i])
for i in range(n-1,0,-1):
    max_[i] = max(max_[i + 1], prefix[i])
#print(prefix)
#print(min_)
#print(max_)
min_[0] = 0
max_[0] = 0

ans = [0]*(n+1)
for i in range(m,n+1):
    ans[i]=max_[i]-min_[i-m]

print(max(ans[1:]))
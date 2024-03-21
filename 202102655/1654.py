import sys
input = sys.stdin.readline
N, K = map(int,input().split())
lis = []
for _ in range(N):
    lis.append(int(input()))

start = 1
end = max(lis)

while start <= end:
    mid = (start + end) // 2
    LAN = 0
    for i in lis:
        LAN += i // mid
    if LAN >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)

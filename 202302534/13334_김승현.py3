from heapq import  heappop,heappush,heapify
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    heappush(hq,a)
d = int(input())

ans = 0
tmp = []
st = 0
end = 0
while hq:
    r, l = heappop(hq)
    heappush(tmp,l)
    end = r
    if end - tmp[0] <= d:
        ans = max(ans, len(tmp))
    else:
        heappop(tmp)
print(ans)
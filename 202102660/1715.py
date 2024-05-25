# 그리디
# 다시 풀기
import sys
import heapq

n = int(sys.stdin.readline())

l = [int(sys.stdin.readline()) for _ in range(n)]

heapq.heapify(l)

total = 0
while len(l)>1:
    # 두개 뽑기
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    
    t = (a + b)
    total += t
    heapq.heappush(l, t)

print(total)
        
    

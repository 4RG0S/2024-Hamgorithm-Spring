import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            min_num = heapq.heappop(heap)
            print(min_num)        
    else:
        heapq.heappush(heap, num)
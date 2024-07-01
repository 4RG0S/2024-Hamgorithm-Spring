import heapq

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda x: x[1])

heapqlist = []
for (name, start, end) in lectures:
    if heapqlist and heapqlist[0] <= start:
        heapq.heappop(heapqlist)
    heapq.heappush(heapqlist, end)
    
print(len(heapqlist))
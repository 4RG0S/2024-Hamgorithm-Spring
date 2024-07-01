import heapq

n, k = map(int, input().split())
INF = float('inf')
arr = [INF] * 100001
arr[n] = 0

def dijkstra(n):
    queue = []
    heapq.heappush(queue, (0, n))
    while queue:
        cost, now = heapq.heappop(queue)    
        if now > 0:
            if arr[now-1] > cost + 1:
                arr[now-1] = cost + 1
                heapq.heappush(queue, (arr[now-1], now-1))
        if now < 100000:
            if arr[now+1] > cost + 1:
                arr[now+1] = cost + 1
                heapq.heappush(queue, (arr[now+1], now+1))
        if 2 * now <= 100000:
            if arr[2 * now] > cost:
                arr[2 * now] = cost
                heapq.heappush(queue, (arr[2 * now], 2 * now))
    return arr[k]

result = dijkstra(n)
print(result)
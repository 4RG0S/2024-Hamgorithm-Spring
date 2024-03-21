import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    visited = [True  for _ in range(k)]
    minQ, maxQ = [], []     # 최소, 최대 힙 따로 생성

    for i in range(k):
        char, n = input().rstrip().split(" ")     # D or I , n 
        n = int(n)

        if char == "I":
            heapq.heappush(maxQ, (-n, i))
            heapq.heappush(minQ, (n, i))
        elif char == "D":
            if n == 1:
                while maxQ and not visited[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    visited[maxQ[0][1]] = False
                    heapq.heappop(maxQ)
            else:
                while minQ and not visited[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    visited[minQ[0][1]] = False
                    heapq.heappop(minQ)

    # 동기화
    while minQ and not visited[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and not visited[maxQ[0][1]]:
        heapq.heappop(maxQ)
    if maxQ and minQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print("EMPTY")


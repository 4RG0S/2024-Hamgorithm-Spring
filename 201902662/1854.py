import sys
import heapq
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))

    cnts = [k for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]

    que = [(0, 1)]
    while que:
        d, p = heapq.heappop(que)
        if cnts[p] > 0:
            cnts[p] -= 1
            if dist[p] <= d:
                dist[p] = d
            else:
                continue
        else:
            continue
        for c, w in edges[p]:
            heapq.heappush(que, (d+w, c))

    for i in range(1, n+1):
        if cnts[i]:
            print(-1)
        else:
            print(dist[i])

if __name__ == "__main__":
    main()
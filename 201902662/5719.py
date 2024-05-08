import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0: break
        start, dest = map(int, input().split())
        
        cost = [[0 for _ in range(n)] for _ in range(n)]
        edge = [[] for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            cost[u][v] = p
            edge[u].append(v)

        path = [[] for _ in range(n)]
        dist = [INF for _ in range(n)]
        dist[start] = 0

        que = [(0, start)]
        while que:
            d, p = heapq.heappop(que)
            if d > dist[p]: continue
            for c in edge[p]:
                nd = d + cost[p][c]
                if nd < dist[c]:
                    path[c] = [p]
                    dist[c] = nd
                    heapq.heappush(que, (nd, c))
                elif nd == dist[c]:
                    path[c].append(p)
        
        que = []
        for p in path[dest]:
            que.append((p, dest))
        while que:
            p, c = que.pop()
            cost[p][c] = INF
            for parent in path[p]:
                if cost[parent][p] == INF:
                    continue
                que.append((parent, p))

        dist = [INF for _ in range(n)]
        dist[start] = 0

        que = [(0, start)]
        while que:
            d, p = heapq.heappop(que)
            if d > dist[p]: continue
            for c in edge[p]:
                nd = d + cost[p][c]
                if nd < dist[c]:
                    dist[c] = nd
                    heapq.heappush(que, (nd, c))

        if dist[dest] == INF:
            print(-1)
        else:
            print(dist[dest])

if __name__ == "__main__":
    main()
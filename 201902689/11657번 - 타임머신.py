import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
edges = []
distance = [INF for _ in range(n + 1)]

def bf(s):
    distance[s] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n-1: return True
    return False


for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i]) if distance[i] != INF else print(-1)
            
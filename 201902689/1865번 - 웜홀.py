import sys
input = sys.stdin.readline
INF = 2000000000

tc = int(input())

def bellmanFord(s):
    distance[s] = 0
    for i in range(n):
        for j in range(2 * m + w):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    distance = [INF for _ in range(n+1)]
    for _ in range(m): # 도로
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w): # 웜홀
        s, e, t = map(int, input().split())
        edges.append((s, e, - t))
    negative_cycle = bellmanFord(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
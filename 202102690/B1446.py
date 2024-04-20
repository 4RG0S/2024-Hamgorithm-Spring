n, d = map(int, input().rstrip().split(' '))
graph = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
distance = [i for i in range(d+1)]

for i in range(d+1) :
    distance[i] = min(distance[i], distance[i-1] + 1)
    for s, e, dist in graph:
        if i == s and e <= d and distance[i] + dist < distance[e] :
            distance[e] = distance[s] + dist

print(distance[d])
import sys

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, input().split()))
    vertex1 = arr[0]
    vertex2 = arr[1]
    index = 1
    while vertex2 != -1:
        cost = arr[index+1]
        graph[vertex1].append((vertex2, cost))
        index += 2
        vertex2 = arr[index]

def dfs(x):
    stack = [x]
    visited = [False] * (v + 1)
    costs = [0] * (v+1)
    while stack:
        node = stack.pop()
        visited[node] = True
        graph[node].sort(key= lambda x : x[1], reverse= True)
        for (n, c) in graph[node]:
            if not visited[n]:
                costs[n] = costs[node] + c
                stack.append(n)
    return costs.index(max(costs)), max(costs)

n, c = dfs(1)
_, result = dfs(n)

print(result)
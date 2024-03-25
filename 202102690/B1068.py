n = int(input())
graph = list(map(int, input().split())) 
d = int(input())

def DFS(node):
    graph[node] = -100
    for i in range(n):
        if node == graph[i]:
            DFS(i)

DFS(d)
count = 0
for i in range(n):
    if (graph[i] != -100) and (i not in graph):
        count += 1
 
print(count)
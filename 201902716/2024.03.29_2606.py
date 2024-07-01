import sys

computer_N = int(sys.stdin.readline().rstrip())
line_N = int(sys.stdin.readline().rstrip())
lines = []

for _ in range(line_N):
    lines.append(list(map(int, sys.stdin.readline().split())))

graph = {i: [] for i in range(1, computer_N + 1)}

for line in lines:
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])


def bfs(start, graph):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += graph[node]

    return visited


print(len(bfs(1, graph)) - 1)

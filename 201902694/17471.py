from collections import deque

def bfs(start, graph, selected, group):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if selected[neighbor] == group and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

def divide(idx, N, graph, peoples, selected):
    if idx == N:
        group_a = [i for i in range(N) if selected[i]]
        group_b = [i for i in range(N) if not selected[i]]

        if not group_a or not group_b:
            return float('inf')

        if bfs(group_a[0], graph, selected, True) == len(group_a) and bfs(group_b[0], graph, selected, False) == len(group_b):
            return abs(sum(peoples[i] for i in group_a) - sum(peoples[i] for i in group_b))
        else:
            return float('inf')

    selected[idx] = True
    res_a = divide(idx + 1, N, graph, peoples, selected)
    selected[idx] = False
    res_b = divide(idx + 1, N, graph, peoples, selected)
    return min(res_a, res_b)

def solve():
    N = int(input())
    peoples = list(map(int, input().split()))
    graph = [[] for _ in range(N)]

    for i in range(N):
        data = list(map(int, input().split()))
        for j in data[1:]:
            graph[i].append(j - 1)

    result = divide(0, N, graph, peoples, [False] * N)
    print(result if result != float('inf') else -1)

if __name__ == "__main__":
    solve()

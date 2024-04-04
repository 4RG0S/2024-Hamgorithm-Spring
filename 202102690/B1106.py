C, N = map(int, input().split())
cost_list = [list(map(int, input().split())) for _ in range(N)]
graph = [1e7 for _ in range(C+100)]
graph[0] = 0
 
for cost, people in cost_list:
    for i in range(people, C+100):
        graph[i] = min(graph[i-people] + cost,graph[i])
 
print(min(graph[C:]))
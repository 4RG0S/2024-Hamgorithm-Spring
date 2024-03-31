from itertools import permutations

N, M, K = map(int, input().split())
Init_adj = [list(map(int, input().split())) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(K)]

def rotate(adj, r, c, s):
    for _ in range(s):
        start_y, start_x = r - s - 1, c - s - 1
        end_y, end_x = r + s - 1, c + s - 1
        prev_value = adj[start_y][start_x]

        for x in range(start_x+1, end_x+1):
            adj[start_y][x], prev_value = prev_value, adj[start_y][x]
        for y in range(start_y+1, end_y+1):
            adj[y][end_x], prev_value = prev_value, adj[y][end_x]
        for x in range(end_x-1, start_x-1, -1):
            adj[end_y][x], prev_value = prev_value, adj[end_y][x]
        for y in range(end_y-1, start_y-1, -1):
            adj[y][start_x], prev_value = prev_value, adj[y][start_x]
        s -= 1

def get_min_value(adj):
    return min(sum(row) for row in adj)

Answer = float('inf')

for perm in permutations(operations):
    adj = [row[:] for row in Init_adj]
    for r, c, s in perm:
        rotate(adj, r, c, s)
    Answer = min(Answer, get_min_value(adj))

print(Answer)

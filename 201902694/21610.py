N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

dY8 = ("skip", 0, -1, -1, -1, 0, 1, 1, 1)
dX8 = ("skip", -1, -1, 0, 1, 1, 1, 0, -1)
dY4, dX4 = (-1, -1, 1, 1), (-1, 1, -1, 1)

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in moves:
    moved = []
    for y, x in clouds:
        ny, nx = (y + dY8[d] * s) % N, (x + dX8[d] * s) % N
        grid[ny][nx] += 1
        moved.append((ny, nx))
    
    for y, x in moved:
        grid[y][x] += sum(1 for dy, dx in zip(dY4, dX4)
                          if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < N and grid[ny][nx] > 0)

    new_clouds = []
    for y in range(N):
        for x in range(N):
            if (y, x) not in moved and grid[y][x] >= 2:
                grid[y][x] -= 2
                new_clouds.append((y, x))
    clouds = new_clouds

print(sum(sum(row) for row in grid))

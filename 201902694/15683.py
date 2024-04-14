def min_blind_spots():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    rows, cols = data[0], data[1]
    grid = [data[i * cols + 2:(i + 1) * cols + 2] for i in range(rows)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cameras = [(i, j) for i in range(rows) for j in range(cols) if 1 <= grid[i][j] <= 5]
    min_spots = [float('inf')]

    def count_spots():
        return sum(1 for i in range(rows) for j in range(cols) if grid[i][j] == 0)

    def apply_cam(x, y, dirs, increment):
        affected = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            while 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 6:
                if grid[nx][ny] == 0:
                    grid[nx][ny] += increment
                    affected.append((nx, ny))
                nx += dx
                ny += dy
        return affected

    def dfs(index):
        if index == len(cameras):
            min_spots[0] = min(min_spots[0], count_spots())
            return
        
        x, y = cameras[index]
        c_type = grid[x][y]

        configs = {
            1: [[0], [1], [2], [3]],
            2: [[0, 1], [2, 3]],
            3: [[0, 2], [2, 1], [1, 3], [3, 0]],
            4: [[0, 2, 1], [2, 1, 3], [1, 3, 0], [3, 0, 2]],
            5: [[0, 1, 2, 3]]
        }

        for config in configs[c_type]:
            affected_areas = [apply_cam(x, y, [dirs[d] for d in config], 1)]
            dfs(index + 1)
            for area in affected_areas:
                for cx, cy in area:
                    grid[cx][cy] -= 1

    dfs(0)
    return min_spots[0]

if __name__ == "__main__":
    print(min_blind_spots())

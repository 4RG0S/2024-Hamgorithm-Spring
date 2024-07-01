import math

t = int(input())
result = []

for _ in range(t):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    for p in range(n):
        cx, cy, r = map(int, input().split())
        d1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        d2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)

        if d1 < r or d2 < r:
            if d1 < r and d2 < r: pass
            else: count += 1

    result.append(count)

for i in result:
    print(i)
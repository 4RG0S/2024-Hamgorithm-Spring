n = int(input())
diff = []
for _ in range(n):
    a, b = map(int, input().split())
    diff.append(b - a)

diff.sort()

result = 0
if len(diff) % 2 == 0:
    result = diff[len(diff) // 2] - diff[len(diff) // 2 - 1] + 1
else:
    result = 1

print(result)
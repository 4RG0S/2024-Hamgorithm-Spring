n = int(input())
a = [[float('inf')] * (n + 1) for _ in range(n + 1)]

while True:
    s1, s2 = map(int, input().split())
    if s1 == -1 and s2 == -1:
        break
    a[s1][s2] = 1
    a[s2][s1] = 1

for i in range(1, n + 1):
    a[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

min_score = float('inf')
score_count = 0
min_score_members = []

for i in range(1, n + 1):
    max_distance = max(a[i][1:])
    if max_distance < min_score:
        min_score = max_distance
        score_count = 1
        min_score_members = [i]
    elif max_distance == min_score:
        score_count += 1
        min_score_members.append(i)

print(min_score, score_count)
print(' '.join(map(str, min_score_members)))
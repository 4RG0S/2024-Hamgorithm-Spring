N = int(input())
scores = []
for _ in range(N):
  line = list(map(int, input().split()))
  scores.append(line)

max_val = 2 ** (N + 1)
minimum = float('inf')
for i in range(max_val):
  start_sum = 0
  link_sum = 0
  for j in range(N):
    team = (i >> j) & 1
    for k in range(N):
      if j != k:
        if (i >> k) & 1 == team:
          if team == 1:
            start_sum += scores[j][k]
          else:
            link_sum += scores[j][k]
    # print(start_sum, link_sum)

  minimum = min(minimum, abs(start_sum - link_sum))

print(minimum)

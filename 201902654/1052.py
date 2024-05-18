N, K = list(map(int, input().split()))

for i in range(K - 1):
  for j in range(24):
    if 2 ** j <= N and 2 ** (j + 1) > N:
      N -= 2 ** j
      break

for j in range(24):
    if 2 ** j >= N:
      print(0)
      break
    if 2 ** j < N and 2 ** (j + 1) > N:
      print(2 ** (j + 1) - N)
      break

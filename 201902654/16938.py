N, L, R, X = list(map(int, input().split()))
A = list(map(int, input().split()))
max_val = 2 ** (N)
result = 0

for i in range(max_val):
  count = 0
  sum_val = 0
  min_val = float('inf')
  max_val = float('-inf')
  for j in range(N):
    if i >> j & 1 == 1:
      value = A[j]
      count += 1
      sum_val += value
      min_val = min(min_val, value)
      max_val = max(max_val, value)
  if count > 1 and sum_val >= L and sum_val <= R and abs(max_val - min_val) >= X:
    result += 1

print(result)

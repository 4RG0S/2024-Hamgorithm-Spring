import copy

weight_count = int(input())
weights = list(map(int, input().split()))

marble_count = int(input())
marbles = list(map(int, input().split()))

can_make_weights = [False for _ in range(80001)]

for i in range(weight_count):
  temp_weight = copy.deepcopy(can_make_weights)
  for j in range(80001):
    added = j + weights[i]
    subed = j - weights[i]
    if j == 40000 + weights[i]:
      temp_weight[j] = True
    if j == 40000 - weights[i]:
      temp_weight[j] = True
    if added < 80001:
      if can_make_weights[added] == True:
        temp_weight[j] = True
    if subed > 0:
      if can_make_weights[subed] == True:
        temp_weight[j] = True
  can_make_weights = temp_weight

for marble in marbles:
  print('Y' if can_make_weights[marble + 40000] == True else 'N', end=' ')

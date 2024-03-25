N = int(input())
global loss_hps
loss_hps = list(map(int, input().split()))
global get_hapinesses
get_hapinesses = list(map(int, input().split()))

result = 0

def recursion(hp_left, hapiness, index, N):
  global loss_hps, get_hapinesses, result
  result = max(result, hapiness)
  if index < N:
    next_hp = hp_left - loss_hps[index]
    # Select
    if next_hp > 0:
      recursion(next_hp, hapiness + get_hapinesses[index], index + 1, N)
    # UnSelect
    recursion(hp_left, hapiness, index + 1, N)

recursion(100, 0, 0, N)

print(result)

N = int(input())

lst = list(map(int, input().split()))
lst.sort()

result_value = float('inf')
result = []

for first in range(len(lst) - 2):
  start_point = first + 1
  compare_point = len(lst) - 1
  while start_point < compare_point:
    value = abs(lst[first] + lst[start_point] + lst[compare_point])
    if value < result_value:
      result_value = value
      result = [lst[first], lst[start_point], lst[compare_point]]
    if compare_point - 1 != start_point and value > abs(lst[first] + lst[start_point] + lst[compare_point - 1]):
      compare_point -= 1
    else:
      start_point += 1

print(result[0], result[1], result[2])

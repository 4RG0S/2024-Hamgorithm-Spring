N = int(input())

lst = list(map(int, input().split()))

result_value = float('inf')
result = []
start_point = 0
compare_point = len(lst) - 1
while start_point < compare_point:
  value = abs(lst[start_point] + lst[compare_point])
  if value < result_value:
    result_value = value
    result = [lst[start_point], lst[compare_point]]
  if compare_point - 1 != start_point and value > abs(lst[start_point] + lst[compare_point - 1]):
    compare_point -= 1
  else:
    start_point += 1

print(result[0], result[1])

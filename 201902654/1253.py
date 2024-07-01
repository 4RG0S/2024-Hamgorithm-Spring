N = int(input())

lst = list(map(int, input().split()))
lst.sort()
dic = {}
for iter in lst:
  if dic.get(iter) == None:
    dic[iter] = 1
  else:
    dic[iter] = dic[iter] + 1
result = 0

for index in range(len(lst)):
  dic[lst[index]] = dic[lst[index]] - 1
  point = 0
  while point < len(lst):
    if point != index:
      val = lst[index] - lst[point]
      if dic.get(val) != None and dic.get(val) > 0:
        if val != lst[point]:
          result += 1
          break
        else:
          if dic[val] > 1:
            result += 1
            break
      point += 1
    else:
      point += 1
  dic[lst[index]] = dic[lst[index]] + 1

print(result)

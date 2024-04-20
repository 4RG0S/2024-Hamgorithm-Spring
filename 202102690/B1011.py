n = int(input())
testcases = [list(map(int, input().split())) for _ in range(n)]
result = []

for tc in testcases:
  count = 0
  x, y = tc
  d = y - x

  while True :
    if d <= count*(count+1) :
      break
    count += 1
  
  if d <= count**2 :
    result.append(count*2-1)
  else :
    result.append(count*2)

for i in result :
  print(i)
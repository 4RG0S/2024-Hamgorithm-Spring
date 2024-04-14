n,d,k,c = map(int, input().split())
plate = []
for i in range(n):
    plate.append(int(input()))

max_sushi = 0
for i in range(n):
    if i <= n-k:
        tmp = set(plate[i:i+k])
    else:
        tmp = set(plate[i:])
        tmp.update(plate[:(i+k)%n])  # %나머지 기호를 잘 사용하자!
    #print(tmp, end=' ')
    tmp.add(c)
    #print(tmp)
    max_sushi = max(max_sushi, len(tmp)) 

print(max_sushi)
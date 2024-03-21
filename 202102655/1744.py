N = int(input())
plus = []
minus = []
result = 0
for _ in range(N):
    get_num = int(input())
    if get_num > 0:
        plus.append(get_num)
    elif get_num <= 0:
        minus.append(get_num)
    
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])
print(result)
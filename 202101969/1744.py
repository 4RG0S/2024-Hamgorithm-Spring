import sys

n = int(sys.stdin.readline())
minus = []
plus = []
one = []
c = 0
for _ in range(n):
    a = int(sys.stdin.readline())
    if a <= 0:
        minus.append(a)
    elif a > 1 :
        plus.append(a)
    elif a ==1:
        one.append(a)
minus.sort()
plus.sort(reverse= True)
s = 0

for i in range(0, len(plus), 2):
    if i+1 == len(plus):
        break
    s += (plus[i] * plus[i+1])
# 길이가 홀수면 마지막꺼 더함
if len(plus) % 2 != 0:
    s += plus[len(plus)-1]
for j in range(0, len(minus), 2):
    if j+1 == len(minus):
        break
    s += (minus[j]*minus[j+1])

if len(minus) % 2 !=0:
    s += minus[len(minus)-1]

print(s+len(one))
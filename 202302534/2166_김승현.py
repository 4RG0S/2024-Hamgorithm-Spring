import sys
input = sys.stdin.readline
# 신발끈공식
# 딱히 좌표들의 정렬이 필요하진 않는다. 외적이용
def Shoelace_formula(n,x, y):
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += x[i] * y[j] - y[i] * x[j]

    area = abs(area) / 2.0

    return area

n = int(input())
x = []
y= []
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

ans = Shoelace_formula(n,x, y)
print(ans)

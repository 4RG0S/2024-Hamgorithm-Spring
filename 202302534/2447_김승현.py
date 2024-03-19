import sys
input = sys.stdin.readline


def star(n):
    if n == 1:
        return "*"

    arr = star(n//3)
    tmp = []
    # 정사각형 모양
    for i in arr:
        tmp.append(i*3)
    for i in arr:
        tmp.append(i+' '*(n//3)+i)  # 3분의 1
    for i in arr:
        tmp.append(i*3)

    return tmp

n = int(input())
#a,b = "***", "* *"
for i in star(n):
    print(i)
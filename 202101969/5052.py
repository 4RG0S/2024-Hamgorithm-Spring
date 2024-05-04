import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())

    number = []
    for _ in range(n):
        number.append(sys.stdin.readline().rstrip())

    number.sort()

    triger = True
    for i in range(len(number) - 1):
        if number[i] == number[i + 1][:len(number[i])]:
            triger = False
            break

    if triger:
        print("YES")
    else:
        print("NO")
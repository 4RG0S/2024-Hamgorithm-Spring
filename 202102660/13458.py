import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

# 1. a (시험장)을 돌면서
# 2. 일단 a가 b 보다 작으면 b 하나만
#   크면 b하나 넣고 나머지에 c
#   (이때 c의 수는 (a-b)//c + 1 if (a-b)%c>0 else (a-b)//c)
count = 0
for students in a:
    count += 1
    if students > b:
        num_c = (students-b)//c
        num_c += 1 if (students-b)%c > 0 else 0
        count += num_c

print(count)

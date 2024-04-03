import sys
input = sys.stdin.readline
num = 246913 # 123456 * 2 + 1
arr = [0] * 2 + [1] * 246912

for i in range(2, num):
    if arr[i]:
        for j in range(i*2, num,i):
            arr[j] = 0

while(1):
    n = int(input())
    if n == 0:
        break

    ans_num = 0
    for i in range(n+1,2*n+1):
        ans_num += arr[i]

    print(ans_num)

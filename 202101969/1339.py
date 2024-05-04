import sys

N = int(sys.stdin.readline())
result = []
dic = dict()
max_num = 0
init = 9
for i in range(N):
    ar = list((input()))
    result.append(ar)

for ar in result:
    for j in range(len(ar)):
        length = len(ar)-j-1
        if ar[j] not in dic:
            dic[ar[j]] = 10 ** length
            continue
        dic[ar[j]] += 10**length
dic = list(dic.values())
dic.sort(reverse=True)

ans = 0
idx = 0

for i in range(9, 9-len(dic), -1):
    ans += dic[idx] * i
    idx += 1
print(ans)
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
check = [False for _ in range(n)]
ans = 0

cnt, cur = 0, 0
while cnt < n:
    for i in range(n):
        if not check[i]:
            cur = i
            break

    while not check[cur]:
        check[cur] = True
        cur = p[cur]
        cnt += 1
        #print(cur)
    # print(check)
    ans += 1
if ans <= 1:
    print(0)
else:
    print(ans)

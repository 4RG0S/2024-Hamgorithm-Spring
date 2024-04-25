import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def power(a,b):
    tmp = 1
    while b > 0:
        if b % 2 == 1:
            tmp = (tmp * a)
        a = (a * a)
        b = b // 2
    return tmp

def bs(x,n):
    low,high =0, 1e9
    while low <= high:
        mid = (low + high)//2
        val = power(mid,x)
        if val >= n:
            high = mid -1
        else:
            low = mid + 1
    return int(low)

def update(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = n-1

    for x in range(1,62):
        m = bs(x, n) # n보다 같거나 큰 m^x
        if m>=n:
            continue

        dic[n] = min(dic[n], update(m)+abs(power(m,x)-n)+1,update(m-1)+abs(power(m-1, x)-n)+1)

    return dic[n]

dic = {1:0}
n = int(input())
print(update(n))

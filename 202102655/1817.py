n, m = map(int, input().split())
if n == 0 :
    print(0)
else :
    data = list(map(int, input().split()))

    target = 0
    result = 1
    for i in range(n-1, -1, -1) :
        target += data[i]
        if target > m :
            result += 1
            target = data[i]

    print(result)
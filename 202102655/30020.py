a, b = map(int, input().split())

patty = a
cheese = b
if cheese >= patty or cheese * 2 < patty:
    print("NO")
    exit()
print("YES")
print(a-b)
while patty > 0:
    if patty == cheese + 1:
        for i in range(patty-1):
            print("ab",end='')
        print("a")
        break
    else:
        print("aba")
        patty -= 2
        cheese -= 1
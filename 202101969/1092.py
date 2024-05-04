import sys
N = int(sys.stdin.readline())
cre = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

cre.sort(reverse=True)
box.sort(reverse=True)

c = 0

if box[0] > cre[0] :
    c = -1
else:
    while box:
        for i in cre:
            if box and i < box[-1]:
                continue
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        c +=1
print(c)
import sys
my, need = map(int, sys.stdin.readline().split())
num = []
for i in range(my):
    temp = int(sys.stdin.readline())
    num.append(temp)
start = 1
end = max(num)
while start <= end:
    mid = (start + end )//2
    c = 0
    for n in num:
        c += n // mid
    if c >= need:
        start = mid +1
    else:
        end = mid -1
print(end)


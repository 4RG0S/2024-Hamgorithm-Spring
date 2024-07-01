n = int(input())
pos = []
min = []

for _ in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    else:
        min.append(num)

pos.sort(reverse = True)
min.sort()

ans = 0
for i in range(1,len(pos),2):
    if pos[i - 1] + pos[i] < pos[i-1] * pos[i]:
        ans += (pos[i - 1] * pos[i])
    else:
        ans += (pos[i - 1] + pos[i])

if len(pos) % 2 != 0:
    ans += pos[-1]

for j in range(1, len(min), 2):
    if min[j - 1] + min[j] < min[j - 1] * min[j]:
        ans += (min[j - 1] * min[j])
    else:
        ans += (min[j - 1] + min[j])

if len(min) % 2 != 0:
    ans += min[-1]

print(ans)
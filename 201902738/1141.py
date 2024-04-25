import sys

N = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

words.sort(key=lambda x: (len(x), x))

result = []
for i in range(N):
    w = words[i]
    chk = False
    for j in range(i + 1, N):
        if words[j].startswith(w):
            chk = True
            break
    if not chk:
        result.append(w)

print(len(result))

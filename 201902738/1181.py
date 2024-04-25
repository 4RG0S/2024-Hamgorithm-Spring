import sys

N = int(sys.stdin.readline())
words = list()
for _ in range(N):
    s = sys.stdin.readline().strip()
    if s not in words:
        words.append(s)

words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)

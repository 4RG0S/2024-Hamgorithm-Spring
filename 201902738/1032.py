import sys

T = int(sys.stdin.readline())
string = []
for _ in range(T):
    s = sys.stdin.readline().strip()
    if not string:
        string = list(s)
    else:
        for i in range(0, len(string)):
            if string[i] != s[i]:
                string[i] = '?'

print(''.join(string))

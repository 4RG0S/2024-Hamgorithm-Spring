import sys

R = 31
M = 1234567891

l = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())

result = 0
for i in range(0, len(s)):
    result += (ord(s[i]) - 96) * R ** i

result %= M
print(result)

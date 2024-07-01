import sys, re

pattern = r'((100+1+)|(01))+'

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().strip()
    if re.fullmatch(pattern, s):
        print("YES")
    else:
        print("NO")
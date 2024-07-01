import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

korean = A // C + (1 if A % C else 0)
math = B // D + (1 if B % D else 0)

print(L - max(korean, math))

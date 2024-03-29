import sys

N = int(sys.stdin.readline())

for i in range(N, 1, -1):
    print((N-i)*" "+(2*i-1)*"*")
for j in range(1, N+1):
    print((N-j)*" "+(2*j-1)*"*")

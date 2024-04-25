import sys

N, K, I = map(int, sys.stdin.readline().strip().split(' '))
cnt = 0
while K != I:
    if K % 2== 0:
        K = K // 2
    else:
        K = (K + 1) // 2
        
    if I % 2 == 0:
        I = I // 2
    else:
        I = (I + 1) // 2
    
    cnt += 1
    
print(cnt)

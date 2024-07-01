import sys

N, L, W, H = map(float, sys.stdin.readline().strip().split(' '))
N = int(N)
end = max(L, W, H)
START = 0
for _ in range(10000):
    mid = (START + end) / 2
    k = (L // mid) * (W // mid) * (H // mid)
    # print('start:', START, 'end:', end)
    # print('mid:', mid, 'k:', k)
    if k >= N:
        START = mid
    else:
        end = mid        

print(f'{end:.10f}')

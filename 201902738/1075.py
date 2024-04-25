N = int(input())
F = int(input())

p = N % 100
Np = N - p
NpF = Np % F
if NpF == 0:
    print('00')
else:
    print(str(F - NpF).zfill(2))

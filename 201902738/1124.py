import sys


def prime_list(n):
    chk = [True] * 100001
    under = [0] * 100001
    for x in range(2, 100001):
        if chk[x]:
            for y in range(x + x, n, x):
                chk[y] = False
                num = y
                while num % x == 0:
                    num //= x
                    under[y] += 1
    # res = {}
    # for z in range(2, n):
    #     if not chk[i]:
    #         res.
    #         res.append([z, under[z]])
    return under, [i for i in range(2, n) if chk[i]]


A, B = map(int, sys.stdin.readline().strip().split(' '))
CNT = 0

under_prime, prime = prime_list(B + 1)
# print(prime)
# print(under_prime)
for i in range(A, B + 1):
    if under_prime[i] in prime:
        CNT += 1
# for i in range(A, B+1):
#     if i in prime:
#         continue
#     else:
#         TMP = 0
#         k = i
#         for j in range(2, int(k ** 0.5) + 1):
#             while k % j == 0:
#                 k //= j
#                 TMP += 1
#         if k != 1:
#             TMP += 1
#     if TMP in prime:
#         CNT += 1

print(CNT)

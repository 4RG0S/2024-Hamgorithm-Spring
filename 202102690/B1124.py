import math

def find_primes(n) :
    length = 0
    for i in range(2, int(n**(1/2))+1):
        while n % i == 0:
            length += 1
            n //= i
    if n != 1:
        length += 1
    return length
    # results = []
    # i = 2

    # while i <= n :
    #     if n == 1 :
    #         break
    #     if n % i == 0 :
    #         results.append(i)
    #         n /= i
    #     else :
    #         i += 1

    # return results

def is_prime(n) :
    for i in range(2, int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    return True

a, b = map(int, input().split())
result = 0

# is_prime = [True for i in range(b + 1)]
 
# is_prime[1] = False
# for i in range(2, b + 1):
#     if not is_prime[i]:
#         continue
    
#     for j in range(i * i, b + 1, i):
#         is_prime[j] = False

for i in range(a, b+1) :
    count = find_primes(i)
    if count != 1 and is_prime(count) :
        result += 1

print(result)
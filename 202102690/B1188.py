import math
n, m = map(int, input().split())
result = m - math.gcd(n, m)
print(result)

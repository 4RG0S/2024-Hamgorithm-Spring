p = 1000000007

fiboMat = {}
fiboMat[1] = [[1, 1], [1, 0]]

def mul(x, y):
    A, B = fiboMat[x], fiboMat[y]
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % p
    matrix[0][1] = (A[0][0]*B[1][0] + A[0][1]*B[1][1]) % p
    matrix[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % p
    matrix[1][1] = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % p
    return matrix

def fibo(n):
    x, y = int(n/2), n-int(n/2)
    if x not in fiboMat: fibo(x)
    if y not in fiboMat: fibo(y)
    fiboMat[n] = mul(x, y)

def gcd(x, y):
    while y != 0:
        temp = x % y
        (x, y) = (y, temp)
    return x

def main():
    n, m = map(int, input().split())
    common = gcd(n, m)
    if common > 1: fibo(common)
    print(fiboMat[common][0][1])

if __name__ == "__main__":
    main()
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

    if x not in fiboMat:
        fibo(x)
    if y not in fiboMat:
        fibo(y)
    
    fiboMat[n] = mul(x, y)

n = int(input())
if n > 1:
    fibo(n)
    print(fiboMat[n][0][1])
else:
    print(1)
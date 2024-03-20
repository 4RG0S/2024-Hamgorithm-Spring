import sys
n = int(sys.stdin.readline())
A = [[1,1],[1,0]]
def mulMatrix(a, b):
    temp = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += a[i][k] * b[k][j]
                temp[i][j] %= 1000000007
    return temp

def fibo(matrix, n):
    if n == 1:
        return matrix
    else:
        result = fibo(matrix, n//2)
        if n % 2 == 0:
            return mulMatrix(result, result)
        else:
            return mulMatrix(mulMatrix(result, result), matrix)

R = fibo(A, n)
if n % 2 == 0:
    print((R[0][0] - 1) % 1000000007)
else:
    print((R[0][1] - 1) % 1000000007)

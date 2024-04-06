n, m = map(int, input().split())
matrix_a = [list(map(int, list(input()))) for _ in range(n)]
matrix_b = [list(map(int, list(input()))) for _ in range(n)]

def change(a, b) :
    for i in range(a, a+3) :
        for j in range(b, b+3) :
            matrix_a[i][j] = 1 - matrix_a[i][j]

if (n < 3 or m < 3) and (matrix_a != matrix_b) :
    print("-1")
else :
    result = 0
    for i in range(n-2):
        for j in range(m-2):
            if matrix_a[i][j] != matrix_b[i][j]:
                result += 1
                change(i, j)

    if matrix_a == matrix_b :
        print(result)
    else :
        print("-1")
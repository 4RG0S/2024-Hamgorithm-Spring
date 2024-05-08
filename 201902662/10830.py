def main():
    n, b = map(int, input().split())
    
    matrices = {}
    result = []
    for i in range(n):
        column = list(map(int, input().split()))
        for j in range(n):
            column[j] = column[j]%1000
        result.append(column)
    matrices[1] = result

    def mul(squareNumber):

        if squareNumber in matrices:
            return

        num1 = int(squareNumber/2)
        num2 = squareNumber - num1
        mul(num1)
        mul(num2)

        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                v = 0
                for k in range(n):
                    v += matrices[num1][i][k] * matrices[num2][k][j]
                result[i][j] = v%1000
        matrices[squareNumber] = result
    
    mul(b)
    for column in matrices[b]:
        print(*column)

if __name__ == "__main__":
    main()
def main():
    n = int(input())
    stars = [[' ' for _ in range(n)] for _ in range(n)]
    
    def fun(x, y, n):
        if n == 1:
            stars[x][y] = '*'
        else:
            nn = int(n/3)
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue
                    fun(x+i*nn, y+j*nn, nn)
            
    fun(0, 0, n)
    for i in range(n):
        for j in range(n):
            print(stars[i][j], end="")
        print()
    
if __name__ == "__main__":
    main()
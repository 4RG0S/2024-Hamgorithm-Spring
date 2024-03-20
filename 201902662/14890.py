def main():
    n, l = map(int, input().split())
    zido = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    
    def canPass(road):
        ramp = [False for i in range(n)]
        for i in range(1, n):
            if road[i] == road[i-1]:
                continue
            elif road[i] - road[i-1] == 1:
                if i-l < 0:
                    return 0
                for j in range(i-l, i):
                    if ramp[j]:
                        return 0
                    ramp[j] = True
            elif road[i] - road[i-1] == -1:
                if i+l > n:
                    return 0
                for j in range(i, i+l):
                    if ramp[j]:
                        return 0
                    ramp[j] = True
            else:
                return 0
        return 1
    
    for i in range(n):
        road1 = zido[i]
        road2 = [zido[j][i] for j in range(n)]
        cnt += canPass(road1)
        cnt += canPass(road2)
    
    print(cnt)
    
if __name__ == "__main__":
    main()
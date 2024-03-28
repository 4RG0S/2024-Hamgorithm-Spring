def main():
    n, a, b = map(int, input().split())
    day, meet = 0, False
    land = [True for i in range(n+1)]
    coor = [a, b]
    
    while coor:
        newCoor = []
        for i in coor:
            iCoor = i + 2**day
            if iCoor <= n:
                if land[iCoor]:
                    land[iCoor] = False
                    newCoor.append(iCoor)
                else:
                    meet = True
                    break
            iCoor = i - 2**day
            if iCoor > 0:
                if land[iCoor]:
                    land[iCoor] = False
                    newCoor.append(iCoor)
                else:
                    meet = True
                    break
        
        day += 1
        coor = newCoor
        if meet:
            break
        
        for i in coor:
            land[i] = True
    
    if meet:
        print(day)
    else:
        print(-1)
    
if __name__ == "__main__":
    main()
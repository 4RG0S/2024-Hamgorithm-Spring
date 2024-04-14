N = int(input())
SK_CY = True

while N>0:
    if N >= 3:
        N -= 3
    else:
        N -=1
    if N != 0:
        SK_CY = not SK_CY
if SK_CY == True:
    print("SK")
else:
    print("CY")
import sys
input = sys.stdin.readline

N = int(input())

def stars(n):
    if n == 1:
        return ['*']

    starlist = stars(n//3)
    arr = []

    for star in starlist:
        arr.append(star*3)
    for star in starlist:
        arr.append(star+' '*(n//3)+star)
    for star in starlist:
        arr.append(star*3)

    return arr

print('\n'.join(stars(N)))
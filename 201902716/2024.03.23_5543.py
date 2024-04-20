import sys

Hadeok = int(sys.stdin.readline())
Jungdeok = int(sys.stdin.readline())
Sangdeok = int(sys.stdin.readline())
Coke = int(sys.stdin.readline())
Sprite = int(sys.stdin.readline())

print(min(Hadeok, Jungdeok, Sangdeok) + min(Coke, Sprite) - 50)

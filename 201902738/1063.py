import sys


def move_piece(direction, piece):
    chk = True
    if direction == 'R':
        if piece[0] + 1 <= 7:
            piece[0] += 1
        else:
            chk = False
    elif direction == 'L':
        if piece[0] - 1 >= 0:
            piece[0] -= 1
        else:
            chk = False
    elif direction == 'B':
        if piece[1] - 1 >= 0:
            piece[1] -= 1
        else:
            chk = False
    elif direction == 'T':
        if piece[1] + 1 <= 7:
            piece[1] += 1
        else:
            chk = False
    elif direction == 'RT':
        if piece[0] + 1 <= 7 and piece[1] + 1 <= 7:
            piece[0] += 1
            piece[1] += 1
        else:
            chk = False
    elif direction == 'LT':
        if piece[0] - 1 >= 0 and piece[1] + 1 <= 7:
            piece[0] -= 1
            piece[1] += 1
        else:
            chk = False
    elif direction == 'RB':
        if piece[0] + 1 <= 7 and piece[1] - 1 >= 0:
            piece[0] += 1
            piece[1] -= 1
        else:
            chk = False
    elif direction == 'LB':
        if piece[0] - 1 >= 0 and piece[1] - 1 >= 0:
            piece[0] -= 1
            piece[1] -= 1
        else:
            chk = False
    return chk


K, S, N = map(str, sys.stdin.readline().strip().split(' '))

King = [int(ord(K[0])) - ord('A'), int(K[1]) - 1]
Stone = [int(ord(S[0])) - ord('A'), int(S[1]) - 1]

for i in range(int(N)):
    move = sys.stdin.readline().strip()
    tmp = King.copy()

    move_piece(move, King)
    if King == Stone:
        if not move_piece(move, Stone):
            King = tmp.copy()


print(chr(King[0] + 65) + str(King[1] + 1))
print(chr(Stone[0] + 65) + str(Stone[1] + 1))

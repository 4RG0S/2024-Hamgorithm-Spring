import sys

N = int(sys.stdin.readline())

card_list = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))

card_dict = {}
for card in card_list:
    card_dict[card] = 1
    
for num in num_list:
    if num in card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')

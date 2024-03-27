import sys
from functools import cmp_to_key
class Pair:
    def __init__(self, num: int, weight, height):
        self.num = num
        self.weight = weight
        self.height = height
        self.rank=1
        
    def __str__(self):
        return str(self.rank)
 
    def setRank(self, rank: int):
        self.rank = rank

def compare_person(me: Pair, other: Pair):
    if (me.weight < other.weight) and (me.height < other.height):
        return True
        
    return False

def compare_person_by_num(p1: Pair, p2: Pair):
    return p1.num - p2.num

N = int(sys.stdin.readline())

pair_list = list()

for i in range(N):
    s = sys.stdin.readline().strip().split()
    w = int(s[0])
    h = int(s[1])
    pair_list.append(Pair(i,w,h))

for i in range(N):
    for j in range(0,N):
        if compare_person(pair_list[i],pair_list[j]):
            pair_list[i].rank+=1

    
ans = " ".join(str(pair) for pair in pair_list)
print(ans)
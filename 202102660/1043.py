import sys

# 1. party 리스트 하나씩 돌면서 알고있는 사람있는지 확인
    # 존재하면 나머지 사람들까지 know 리스트에 넣기 (중복 제거)
# 2. party 리스트 하나씩 다시 돌면서 알고 있는 사람 존재하는지 다시 확인

N, M = map(int, sys.stdin.readline().split())
know = set(list(map(int, sys.stdin.readline().split()))[1:])

party = [set(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(M)]

# 파티 수만큼 반복해야하는 이유!
# : 1. 매 파티마다 새롭게 know리스트에 추가되는 사람이 있을 수 있음.
#   2. 그러면 이미 지나갔던 파티에 그 사람과 know 리스트에 없는 사람. 이렇게 둘이 있던 경우도 존재.
#   -> 반복 안하면 저 파티의 사람들은 know 리스트에 추가가 안됨.
#   추가되는 과정에서 또 2번 과정이 반복됨. --> 파티 수만큼 반복해야함.
for _ in range(M):
    for p in party:
        print(p)
        if p & know:
            know = know.union(p)
            # print(know)

cant = 0
for p in party:
    if p & know:
        cant += 1

print(M-cant) 

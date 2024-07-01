import sys

N, M = map(int, sys.stdin.readline().strip().split())

pokemon_dict = {}

for i in range(N):
    pokemon = sys.stdin.readline().strip()
    pokemon_dict[pokemon] = str(i + 1)
    pokemon_dict[str(i + 1)] = pokemon

for _ in range(M):
    input = sys.stdin.readline().strip()
    print(pokemon_dict[input])

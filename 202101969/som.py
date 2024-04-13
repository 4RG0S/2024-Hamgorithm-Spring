import sys
H, W = map(int, sys.stdin.readline().split())
rain_Map = list(map(int, sys.stdin.readline().split()))
rain  = 0
for i in range(1, W-1):
    # 양 끝단에는 빗물이 고일 수 없으니 안 봐도 됌.
    left = max(rain_Map[:i])
    right = max(rain_Map[i+1:])
    moreLow = min(left, right)

    if moreLow > rain_Map[i]: #지금 보고 있는게 벽 보다 작아야 고임.
        rain += (moreLow - rain_Map[i])
print(rain)

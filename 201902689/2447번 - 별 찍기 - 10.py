import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def draw_stars(n):
    if n == 1:
        return ['*']

    stars = draw_stars(n//3)
    lines = []

    for star in stars:  # 1번째 라인
        lines.append(star * 3)
    for star in stars:  # 2번째 라인
        lines.append(star + ' ' * (n // 3) + star)
    for star in stars:  # 3번째 라인
        lines.append(star * 3)

    return lines

n = int(input())
result = draw_stars(n)
print("\n".join(result))
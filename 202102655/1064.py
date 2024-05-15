# 1064번 - 평행사변형

ax, ay, bx, by, cx, cy = map(int, input().split())

if (ax - bx) * (cy - by) == (ay - by) * (cx - bx):
    print(-1)
    exit()

ab_length = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
bc_length = ((cx - bx) ** 2 + (cy - by) ** 2) ** 0.5
ac_length = ((ax - cx) ** 2 + (ay - cy) ** 2) ** 0.5

length = [ab_length+ac_length, ab_length+bc_length, ac_length+bc_length]
result = max(length) - min(length)
print(result * 2)
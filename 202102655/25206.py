rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	# 학점 총합을 담을 변수
result = 0	# (학점 * 과목평점) 총합을 담을 변수
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	# 등급이 P인 과목은 계산 안함
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result / total))
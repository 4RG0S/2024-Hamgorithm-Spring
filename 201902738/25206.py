import sys

score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

sum_credits = 0
sum_grade = 0
for _ in range(20):
    name, credit, rank = map(str, sys.stdin.readline().strip().split())
    if rank != "P":
        sum_credits += float(credit)
        sum_grade += score[rank] * float(credit)

print("%.6f" % (sum_grade / sum_credits))

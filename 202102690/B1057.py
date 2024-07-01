n, a, b = map(int, input().split())
count = 0 

while True :
	a -= a//2
	b -= b//2
	count += 1
	if a == b:
		break

print(count)
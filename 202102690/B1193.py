X = int(input())
count = 1

while X > count:
    X -= count
    count += 1

if count % 2 == 0:
    a = X
    b = count - X + 1 
else:
    a = count - X + 1
    b = X

print(f"{a}/{b}")
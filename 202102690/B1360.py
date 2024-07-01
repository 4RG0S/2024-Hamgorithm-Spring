n = int(input())
queue = []
now = ''

for _ in range(n):
    flag = False
    command, char, num = map(str, input().split())

    if command == 'type':
        now += char
        queue.append((int(num), now))
    else:
        char, num = int(char), int(num)
        
        for i in range(len(queue)-1, -1, -1):
            if queue[i][0] >= num - char :
                continue
            flag = True
            now = queue[i][1]
            queue.append((num, now))
            break

        if not flag:
            now = ''
            queue.append((num, now))

print(queue[-1][1])
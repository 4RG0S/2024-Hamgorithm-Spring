N, K = map(int, input().split())
belts = list(map(int, input().split()))
robots = [False] * N 

def rotate():
    global belts, robots
    last_belt = belts.pop()
    last_robot = robots.pop()
    belts.insert(0, last_belt)
    robots.insert(0, last_robot)
    if robots[N-1]:
        robots[N-1] = False

def move_robots():
    for i in range(N-2, -1, -1): 
        if robots[i] and not robots[i+1] and belts[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belts[i+1] -= 1
    if robots[N-1]: 
        robots[N-1] = False

def insert_robot():
    if belts[0] > 0: 
        robots[0] = True
        belts[0] -= 1

def is_finish():
    return belts.count(0) >= K

cnt = 0
while not is_finish():
    cnt += 1
    rotate()
    move_robots()
    insert_robot()

print(cnt)

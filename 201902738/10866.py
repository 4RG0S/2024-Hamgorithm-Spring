import sys

N = int(sys.stdin.readline())
deque = list()

for _ in range(N):
    input = sys.stdin.readline().strip().split()
    match input[0]:
        case "push_front":
            deque.insert(0, input[1])
        case "push_back":
            deque.append(input[1])
        case "pop_front":
            print(deque.pop(0) if deque else -1)
        case "pop_back":
            print(deque.pop() if deque else -1)
        case "size":
            print(len(deque))
        case "empty":
            print(0 if deque else 1)
        case "front":
            print(deque[0] if deque else -1)
        case "back":
            print(deque[-1] if deque else -1)
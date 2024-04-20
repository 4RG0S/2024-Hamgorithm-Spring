import Foundation

var n = Int(readLine()!)!
var queue: [Int] = []
for _ in 0..<n {
    let input = readLine()!
    let command = input.components(separatedBy: " ")
    if command.count == 2 {
        order(op: command[0], num: Int(command[1])!)
    } else {
        order(op: command[0])
    }
}

func order(op: String, num: Int) {
    switch op {
        case "push":
            queue.append(num)
            break
    default: break
        
    }
}

func order(op: String) {
    switch op {
    case "pop":
        if queue.isEmpty {
            print(-1)
            break
        }
        let num = queue.removeFirst()
        print(num)
        break
    case "size":
        print(queue.count)
        break
    case "empty":
        if queue.isEmpty {
            print(1)
        } else {
            print(0)
        }
        break
    case "front":
        if queue.isEmpty {
            print(-1)
            break
        }
        print(queue[0])
        break
    case "back":
        if let last = queue.last {
            print(last)
        } else {
            print(-1)
        }
        break
    default : break
    }
}

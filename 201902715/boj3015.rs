fn read_int_from_line() -> i64 {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf).unwrap();
    buf.trim().parse::<i64>().unwrap()
}

pub fn main() {
    let n = read_int_from_line();
    let mut arr: Vec<(i64, i64)> = Vec::new();
    arr.push((read_int_from_line(), 1));
    // let mut count: i64 = 0;

    for _ in 1..n {
        let new_person = read_int_from_line();
        let last_person_in_stack = arr.last().unwrap();

        if last_person_in_stack.0 == new_person {
            let (height, count) = arr.pop().unwrap();
            arr.push((height, count + 1));
        } else {
            arr.push((new_person, 1));
        }
    }

    // println!("input : {:?}", arr);

    let mut sum = 0;
    let mut stack: Vec<(i64, i64)> = Vec::new(); // height 내림차순으로만 저장
    stack.push(*arr.get(0).unwrap());
    for i in 1..arr.len() {
        // println!("stack : {:?}", stack);

        let (height, mut count) = *arr.get(i).unwrap();
        let (mut last_height, mut last_count) = stack.last().unwrap();
        if last_height > height {
        } else if last_height < height {
            while last_height < height {
                stack.pop();
                sum += if stack.is_empty() {
                    last_count
                } else {
                    last_count * 2
                };
                sum += (last_count * (last_count - 1)) / 2;
                if stack.is_empty() {
                    break;
                }
                (last_height, last_count) = *stack.last().unwrap();
            }
        }

        if last_height == height {
            while last_height == height {
                stack.pop();
                count += last_count;
                if stack.is_empty() {
                    break;
                }
                (last_height, last_count) = *stack.last().unwrap();
            }
        }

        stack.push((height, count));
    }

    while !stack.is_empty() {
        let (_, count) = stack.pop().unwrap();
        sum += if stack.is_empty() { 0 } else { count };
        sum += (count * (count - 1)) / 2;
    }

    // println!("sum : {}", sum);
    // println!("stack : {:?}", stack);
    
    println!("{}", sum);
}

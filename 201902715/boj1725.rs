fn read_int_from_line() -> i64 {
    let stdin = std::io::stdin();
    let mut buf = String::new();

    stdin.read_line(&mut buf).unwrap();

    buf.trim().parse().unwrap()
}

pub fn main() {
    let n = read_int_from_line();
    let mut histogram: Vec<i64> = Vec::new();
    for _ in 0..n {
        histogram.push(read_int_from_line());
    }
    histogram.push(0);

    let mut stack: Vec<(usize, i64)> = Vec::new();
    let mut answer: i64 = 0;

    for index in 0..histogram.len() {
        while !stack.is_empty() && stack.last().unwrap().1 > histogram[index] {
            let (last_index, last_height) = stack.pop().unwrap();
            let width = if stack.is_empty() {
                index as i64
            } else {
                (index - stack.last().unwrap().0 - 1) as i64
            };
            answer = answer.max(width * last_height);
        }
        stack.push((index, histogram[index]));
    }

    println!("{}", answer);
}

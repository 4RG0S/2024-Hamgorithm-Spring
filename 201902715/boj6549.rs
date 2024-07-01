pub fn main() {
    loop {
        let stdin = std::io::stdin();
        let mut line = String::new();
        stdin.read_line(&mut line).unwrap();
        let n = line.trim().parse::<usize>();
        if n.is_ok_and(|n| n == 0) {
            break;
        }

        let mut histogram: Vec<i64> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
        histogram.remove(0);
        histogram.push(0);

        let mut stack: Vec<(usize, i64)> = Vec::new();
        let mut answer: i64 = 0;

        for index in 0..histogram.len() {
            while !stack.is_empty() && stack.last().unwrap().1 > histogram[index] {
                let (_, last_height) = stack.pop().unwrap();
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
}

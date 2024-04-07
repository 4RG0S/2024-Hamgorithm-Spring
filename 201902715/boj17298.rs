use std::io::{BufWriter, Write};

pub fn main() {
    let stdin = std::io::stdin();
    let mut out = BufWriter::new(std::io::stdout().lock());
    let mut buf = String::new();
    stdin.read_line(&mut buf).unwrap();

    let n: i32 = buf.trim().parse().unwrap();
    buf.clear();

    let a = {
        stdin.read_line(&mut buf).unwrap();
        buf.split_whitespace().map(|x| x.parse::<i32>().unwrap())
    };

    let mut result = [-1; 1_000_000];
    let mut stack: Vec<(usize, i32)> = Vec::new();
    for (i, elem) in a.enumerate() {
        if stack.last().is_none() || (stack.last().is_some() && stack.last().unwrap().1 >= elem) {
        } else {
            loop {
                // 현재 바라보고 있는 원ㅅ와 stack에 들어있는 원소들을 꺼내면서 비교해서 result에 채워넣기
                if stack.last().is_some() && (stack.last().unwrap().1 < elem) {
                    let last = stack.pop().unwrap();
                    result[last.0] = elem;
                } else {
                    break;
                }
            }
        }
        stack.push((i, elem));
    }

    for i in 0..n {
        write!(out, "{} ", result[i as usize]).unwrap();
    }
}

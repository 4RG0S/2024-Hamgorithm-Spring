use std::io::{self, Write};

fn read_int(n: i8) -> Vec<i32> {
    assert!(n >= 1, "n should be equal to or larger than 1");

    let mut result: Vec<i32> = Vec::new();

    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();

    if n == 1 {
        result.push(buf.trim().parse::<i32>().unwrap());
        return result;
    } else {
        return buf
            .split(" ")
            .map(|c| c.trim().parse().unwrap())
            .collect::<Vec<i32>>();
    }
}

pub fn main() {
    let stdout = io::stdout();
    let mut out = std::io::BufWriter::new(stdout.lock());

    let t = *read_int(1).get(0).unwrap();
    for _ in 0..t {
        let numbers = read_int(2);
        let a = numbers.get(0).unwrap();
        let b = numbers.get(1).unwrap();
        writeln!(out, "{}", a + b).unwrap();
    }
}

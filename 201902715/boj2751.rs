use std::io::Write;
use std::io::BufWriter;

pub fn main() {
    let mut buf = String::new();
    let stdin = std::io::stdin();
    let mut out = BufWriter::new(std::io::stdout().lock());

    stdin.read_line(&mut buf).unwrap();

    let n = buf.trim().parse::<i32>().unwrap();
    let mut arr: Vec<i32> = Vec::new();
    for _ in 0..n {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        arr.push(buf.trim().parse::<i32>().unwrap());
    }

    arr.sort();
    for elem in arr.iter() {
        writeln!(out, "{}", elem).unwrap();
    }
}

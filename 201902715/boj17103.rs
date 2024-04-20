use std::io::Write;
use std::io::BufWriter;

pub fn main() {
    let mut prime_arr = [true; 1_000_001];
    prime_arr[0] = false;
    prime_arr[1] = false;

    for i in 2..prime_arr.len() {
        if prime_arr[i] == false {
            continue;
        }

        for j in 2.. {
            if i * j >= prime_arr.len() {
                break;
            }

            prime_arr[i * j] = false;
        }
    }

    let stdin = std::io::stdin();
    let mut buf = String::new();
    let mut out = BufWriter::new(std::io::stdout().lock());

    stdin.read_line(&mut buf).unwrap();
    let t: i32 = buf.trim().parse().unwrap();

    for _ in 0..t {
        buf.clear();
        stdin.read_line(&mut buf).unwrap();
        let n: i32 = buf.trim().parse().unwrap();
        let mut partitions = 0;

        for i in 2.. {
            if i * 2 > n {
                break;
            }

            if prime_arr[i as usize] == false {
                continue;
            }

            if prime_arr[(n - i) as usize] {
                partitions += 1;
            }
        }

        writeln!(out, "{}", partitions).unwrap();
    }
}
